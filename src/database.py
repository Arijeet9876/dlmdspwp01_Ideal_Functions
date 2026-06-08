"""
Database operations using SQLAlchemy.
"""

import pandas as pd
from sqlalchemy import create_engine

from .base import BaseComponent
from .exceptions import DatabaseError


class DatabaseManager(BaseComponent):
    """
    Handles SQLite database operations.
    """

    def __init__(
        self,
        db_path: str = "output/results.db"
    ):
        self.db_path = db_path

        self.engine = create_engine(
            f"sqlite:///{self.db_path}"
        )

    def save_dataframe(
        self,
        dataframe: pd.DataFrame,
        table_name: str
    ) -> None:
        """
        Save DataFrame to SQLite.
        """

        try:

            self.log(
                f"Saving table {table_name}"
            )

            dataframe.to_sql(
                table_name,
                self.engine,
                if_exists="replace",
                index=False
            )

        except Exception as error:

            raise DatabaseError(
                f"Failed to save {table_name}: {error}"
            )