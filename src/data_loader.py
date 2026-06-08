"""
Loads project datasets from CSV files.
"""

from pathlib import Path

import pandas as pd

from .base import BaseComponent
from .exceptions import DataLoadError


class DataLoader(BaseComponent):
    """
    Loads training, ideal, and test datasets.
    """

    def __init__(self, data_folder: str = "data"):
        self.data_folder = Path(data_folder)

    def load_training_data(self) -> pd.DataFrame:
        """
        Load training dataset.
        """
        try:
            file_path = self.data_folder / "train.csv"

            self.log(f"Loading {file_path}")

            return pd.read_csv(file_path)

        except Exception as error:
            raise DataLoadError(
                f"Failed to load training data: {error}"
            )

    def load_ideal_data(self) -> pd.DataFrame:
        """
        Load ideal functions dataset.
        """
        try:
            file_path = self.data_folder / "ideal.csv"

            self.log(f"Loading {file_path}")

            return pd.read_csv(file_path)

        except Exception as error:
            raise DataLoadError(
                f"Failed to load ideal data: {error}"
            )

    def load_test_data(self) -> pd.DataFrame:
        """
        Load test dataset.
        """
        try:
            file_path = self.data_folder / "test.csv"

            self.log(f"Loading {file_path}")

            return pd.read_csv(file_path)

        except Exception as error:
            raise DataLoadError(
                f"Failed to load test data: {error}"
            )