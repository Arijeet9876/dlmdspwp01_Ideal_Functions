import pandas as pd

from src.function_selector import FunctionSelector


def test_best_function_selection():

    training_df = pd.read_csv("data/train.csv")
    ideal_df = pd.read_csv("data/ideal.csv")

    selector = FunctionSelector()

    selected_functions, _ = (
        selector.select_best_functions(
            training_df,
            ideal_df
        )
    )

    assert selected_functions["y1"] == "y13"
    assert selected_functions["y2"] == "y24"
    assert selected_functions["y3"] == "y36"
    assert selected_functions["y4"] == "y40"