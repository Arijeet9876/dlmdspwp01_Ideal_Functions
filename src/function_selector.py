"""
Selects the best ideal functions using least squares.
"""

import numpy as np
import pandas as pd

from .base import BaseComponent
from .exceptions import FunctionSelectionError

class FunctionSelector(BaseComponent):
    """
    Selects ideal functions for training datasets.
    """

    def select_best_functions(
        self,
        training_df: pd.DataFrame,
        ideal_df: pd.DataFrame
    ):
        """
        Find best ideal function for each training function.
        """

        try:
            selected_functions = {}
            max_deviations = {}

            training_columns = [
                "y1",
                "y2",
                "y3",
                "y4"
            ]

            ideal_columns = [
                col
                for col in ideal_df.columns
                if col != "x"
            ]

            for train_col in training_columns:

                best_sse = float("inf")
                best_function = None
                best_deviation = None

                train_values = training_df[train_col]

                for ideal_col in ideal_columns:

                    ideal_values = ideal_df[ideal_col]

                    sse = np.sum(
                        (train_values - ideal_values) ** 2
                    )

                    if sse < best_sse:

                        best_sse = sse

                        best_function = ideal_col

                        best_deviation = np.max(
                            np.abs(
                                train_values
                                - ideal_values
                            )
                        )

                selected_functions[
                    train_col
                ] = best_function

                max_deviations[
                    train_col
                ] = best_deviation

                self.log(
    f"{train_col} -> {best_function} "
    f"(max deviation: {best_deviation:.4f})"
)

            return (
                selected_functions,
                max_deviations
            )

        except Exception as error:

            raise FunctionSelectionError(
                f"Selection failed: {error}"
            )