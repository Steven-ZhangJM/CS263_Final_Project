import pandas as pd

# Load the main dataframe
results_df = pd.read_csv("evaluation_results.csv")

# Load the prompt dataframes
prompt_df_llama3 = pd.read_csv("prompt_df_llama3.csv")
prompt_df_gpt4 = pd.read_csv("prompt_df_gpt4.csv")
prompt_df_code_gen = pd.read_csv("prompt_df_code_gen.csv")


results_df["llama3_final"] = 0
results_df["gpt4_final"] = 0
results_df["code_gen_final"] = 0

# Sum the scores for each row in the main dataframe
for idx, row in results_df.iterrows():

    results_df.at[idx, "llama3_final"] = (
        row["llama3"] * 0.6
        + prompt_df_llama3.loc[idx, "correctness"] * 0.2 / 5
        + (
            prompt_df_llama3.loc[idx, "efficiency"]
            + prompt_df_llama3.loc[idx, "readability"]
        )
        * 0.1
        / 5
    )

    results_df.at[idx, "gpt4_final"] = (
        row["gpt4"] * 0.6
        + prompt_df_gpt4.loc[idx, "correctness"] * 0.2 / 5
        + (
            prompt_df_gpt4.loc[idx, "efficiency"]
            + prompt_df_gpt4.loc[idx, "readability"]
        )
        * 0.1
        / 5
    )

    results_df.at[idx, "code_gen_final"] = (
        row["code_gen"] * 0.6
        + prompt_df_code_gen.loc[idx, "correctness"] * 0.2 / 5
        + (
            prompt_df_code_gen.loc[idx, "efficiency"]
            + prompt_df_code_gen.loc[idx, "readability"]
        )
        * 0.1
        / 5
    )

# Save the updated dataframe to a new CSV file
results_df.to_csv("evaluation_results_final.csv", index=False)
