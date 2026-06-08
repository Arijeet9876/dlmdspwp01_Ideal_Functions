import pandas as pd

from src.mapper import Mapper
from src.function_selector import (
    FunctionSelector
)


def test_mapping_returns_dataframe():

    train_df = pd.read_csv(
        "data/train.csv"
    )

    ideal_df = pd.read_csv(
        "data/ideal.csv"
    )

    test_df = pd.read_csv(
        "data/test.csv"
    )

    selector = FunctionSelector()

    (
        selected_functions,
        max_deviations
    ) = selector.select_best_functions(
        train_df,
        ideal_df
    )

    mapper = Mapper()

    mapped_df = mapper.map_test_data(
        test_df,
        ideal_df,
        selected_functions,
        max_deviations
    )

    assert len(mapped_df) > 0