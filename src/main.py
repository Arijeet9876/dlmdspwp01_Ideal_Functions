"""
Main entry point for the project.
"""

from .data_loader import DataLoader
from .database import DatabaseManager
from .function_selector import FunctionSelector
from .mapper import Mapper
from .visualizer import Visualizer


def main():
    """
    Execute complete workflow.
    """

    loader = DataLoader()

    train_df = loader.load_training_data()
    ideal_df = loader.load_ideal_data()
    test_df = loader.load_test_data()

    db = DatabaseManager()

    db.save_dataframe(
        train_df,
        "training_data"
    )

    db.save_dataframe(
        ideal_df,
        "ideal_functions"
    )

    selector = FunctionSelector()

    (
        selected_functions,
        max_deviations
    ) = selector.select_best_functions(
        train_df,
        ideal_df
    )

    print("\nSelected Functions:")
    print(selected_functions)

    mapper = Mapper()

    mapped_df = mapper.map_test_data(
        test_df,
        ideal_df,
        selected_functions,
        max_deviations
    )

    visualizer = Visualizer()

    visualizer.plot_training_data(
        train_df
    )

    visualizer.plot_selected_functions(
        ideal_df,
        selected_functions
    )

    visualizer.plot_mapping_results(
        mapped_df
    )

    db.save_dataframe(
        mapped_df,
        "test_results"
    )

    print(
        f"\nMapped points: {len(mapped_df)}"
    )

    print(
        "\nWorkflow completed successfully."
    )


if __name__ == "__main__":
    main()