import pandas as pd

from src.database import DatabaseManager


def test_database_save():

    db = DatabaseManager(
        "output/test_results.db"
    )

    dataframe = pd.DataFrame(
        {
            "x": [1, 2],
            "y": [3, 4]
        }
    )

    db.save_dataframe(
        dataframe,
        "sample_table"
    )

    assert True