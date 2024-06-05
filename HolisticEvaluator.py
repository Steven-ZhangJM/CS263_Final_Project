import os
import ollama
import subprocess
import re
import pandas as pd
from Evaluator import Evaluator
import ProblemSetReader


class HolisticEvaluator(Evaluator):
    def __init__(self):
        super().__init__()

    def evaluate_pass_at_k(self, folder_path, problem_set_df, k=1, verbose=False):
        ret_dict = {"pass_at_k_count": 0, "total_count": 0}

        geval_idxes = []

        for idx in problem_set_df["idx"].values:
            correct_found = False

            for attempt in range(k):
                file_name = f"p{idx:03d}_{attempt}.py"
                code_path = os.path.join(folder_path, file_name)

                if not os.path.exists(code_path):
                    continue

                answer_truth = problem_set_df[problem_set_df["idx"] == idx][
                    "answer"
                ].values[0]
                result = self.evaluate_subprocess(code_path, answer_truth, verbose)

                if result == "correct answer":
                    correct_found = True
                    geval_idxes.append(idx)
                    break

            ret_dict["total_count"] += 1
            if correct_found:
                ret_dict["pass_at_k_count"] += 1
            else:
                geval_idxes.append(0)

        ret_dict["pass_at_k_ratio"] = (
            ret_dict["pass_at_k_count"] / ret_dict["total_count"]
        )
        print("Pass@K: ", ret_dict["pass_at_k_ratio"])
        return ret_dict, geval_idxes

    def parse_output(self, output):
        correctness = efficiency = readability = 0
        try:
            correctness = int(re.search(r"\*\*Correctness:\*\* (\d+)", output).group(1))
            efficiency = int(re.search(r"\*\*Efficiency:\*\* (\d+)", output).group(1))
            readability = int(re.search(r"\*\*Readability:\*\* (\d+)", output).group(1))
        except AttributeError:
            print(f"Failed to parse output: {output}")
            raise ValueError("Parsing failed")
        return correctness, efficiency, readability

    def get_Geval_output(self, prompt):
        answer = ollama.generate(model="llama3", prompt=prompt)["response"]
        return answer

    def Geval(self, df, k):
        max_retries = 5
        for index, row in df.iterrows():
            for i in range(k):
                prompt = row["prompt"]
                retries = 0
                success = False

                while retries < max_retries and not success:
                    try:
                        output = self.get_Geval_output(prompt)
                        correctness, efficiency, readability = self.parse_output(output)
                        df.at[index, "correctness"] += correctness
                        df.at[index, "efficiency"] += efficiency
                        df.at[index, "readability"] += readability
                        success = True
                    except Exception as e:
                        retries += 1
                        print(
                            f"Retry {retries}/{max_retries} for prompt: {prompt}. Error: {e}"
                        )

            df.at[index, "correctness"] /= k
            df.at[index, "efficiency"] /= k
            df.at[index, "readability"] /= k
        return df

    def create_prompts(self, prom_template_path, answers_folder, df):
        with open(prom_template_path, "r", encoding="utf-8") as Geval_file:
            prompt_template = Geval_file.read()

        prompts_list = []

        for index, row in df.iterrows():
            question_id = row["idx"]
            description = row["question"]
            truth = row["python_code"]

            answer_file_path = os.path.join(answers_folder, f"p{question_id:03d}.py")

            with open(answer_file_path, "r") as answer_file:
                answer = answer_file.read()

                prompt = (
                    prompt_template.replace("{{Question}}", description)
                    .replace("{{Answer}}", answer)
                    .replace("{{Truth}}", truth)
                )
                prompts_list.append({"question_id": question_id, "prompt": prompt})

            prompts_df = pd.DataFrame(prompts_list)
            prompts_df["correctness"] = 0
            prompts_df["efficiency"] = 0
            prompts_df["readability"] = 0

        return prompts_df

    def create_prompts_better(
        self, prom_template_path, answers_folder, df, geval_idxes=None
    ):
        with open(prom_template_path, "r", encoding="utf-8") as Geval_file:
            prompt_template = Geval_file.read()

        prompts_list = []

        for index, row in df.iterrows():
            question_id = row["idx"]
            description = row["question"]
            truth = row["python_code"]

            if geval_idxes is None:
                answer_file_path = os.path.join(
                    answers_folder, f"p{question_id:03d}.py"
                )
            else:
                answer_file_path = os.path.join(
                    answers_folder, f"p{question_id:03d}_{geval_idxes[index]}.py"
                )

            with open(answer_file_path, "r") as answer_file:
                answer = answer_file.read()

                result = self.evaluate_subprocess(answer_file_path, row["answer"])

                prompt = (
                    prompt_template.replace("{{Question}}", description)
                    .replace("{{Answer}}", answer)
                    .replace("{{Result}}", result)
                    .replace("{{Truth}}", truth)
                )
                prompts_list.append({"question_id": question_id, "prompt": prompt})

            prompts_df = pd.DataFrame(prompts_list)
            prompts_df["correctness"] = 0
            prompts_df["efficiency"] = 0
            prompts_df["readability"] = 0

        return prompts_df

    def print_average_metrics(self, df):
        avg_correctness = df["correctness"].mean()
        avg_efficiency = df["efficiency"].mean()
        avg_readability = df["readability"].mean()

        print(f"Correctness Average: {avg_correctness}")
        print(f"Efficiency Average: {avg_efficiency}")
        print(f"Readability Average: {avg_readability}")
