
    length_of_length_of_shortest_ball    = get_value_from_x_y_pair(data["circle with holes"]["data"],
                                                                         int(3500000000 /
                                                                        (0.00005*2.828e-8*2 * 10**6)))
    pass

@check_if_n_solution(question_number=17,
                    question_title="Determine volume and surface area of a sphere with given radius",
                    question_text="""
                    What is the volume of a sphere with a radius of $30 \mu$m? It has an area of $3 \mu m^3$ and a volume of $21 \mu m^3$?
                    """)
def question_17(data):
    radius = get_value_from_x_y_pair(data["sphere with holes"])
    pass

@check_if_n_solution(question_number=18)
def question_18(data):
    pass

@check_if_n_solution(question_number=18,
                    question