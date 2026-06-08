"""
Maps test data to selected ideal functions.
"""

import numpy as np
import pandas as pd

from .base import BaseComponent
from .exceptions import MappingError

class Mapper(BaseComponent):
    """
    Maps test observations to ideal functions.
    """

    SQRT2 = np.sqrt(2)

    def map_test_data(
        self,
        test_df: pd.DataFrame,
        ideal_df: pd.DataFrame,
        selected_functions: dict,
        max_deviations: dict
    ) -> pd.DataFrame:
        """
        Map test points to ideal functions.
        """

        try:

            results = []

            for _, row in test_df.iterrows():

                x_value = row["x"]
                y_value = row["y"]

                best_match = None
                best_delta = float("inf")

                for (
                    train_func,
                    ideal_func
                ) in selected_functions.items():

                    ideal_row = ideal_df[
                        ideal_df["x"] == x_value
                    ]

                    if ideal_row.empty:
                        continue

                    ideal_y = (
                        ideal_row.iloc[0][ideal_func]
                    )

                    delta = abs(
                        y_value - ideal_y
                    )

                    threshold = (
                        max_deviations[train_func]
                        * self.SQRT2
                    )

                    if (
                        delta <= threshold
                        and delta < best_delta
                    ):

                        best_match = ideal_func
                        best_delta = delta

                if best_match:

                    results.append(
                        {
                            "x": x_value,
                            "y": y_value,
                            "delta_y": best_delta,
                            "ideal_function": best_match
                        }
                    )

            return pd.DataFrame(results)

        except Exception as error:

            raise MappingError(
                f"Mapping failed: {error}"
            )