"""
Visualization module using Bokeh.
"""

from pathlib import Path

from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import save

from .base import BaseComponent


class Visualizer(BaseComponent):
    """
    Creates project visualizations.
    """

    def __init__(
        self,
        output_folder: str = "output/plots"
    ):
        self.output_folder = Path(output_folder)

        self.output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    def plot_training_data(
        self,
        training_df: pd.DataFrame
    ) -> None:
        """
        Plot training functions.
        """

        output_file(
            self.output_folder
            / "training_data.html"
        )

        plot = figure(
            title="Training Data"
        )

        colors = [
            "blue",
            "red",
            "green",
            "purple"
        ]

        for index, column in enumerate(
            ["y1", "y2", "y3", "y4"]
        ):

            plot.line(
                training_df["x"],
                training_df[column],
                color=colors[index],
                legend_label=column,
                line_width=2
            )

        save(plot)

        self.log(
            "Training plot created"
        )

    def plot_selected_functions(
        self,
        ideal_df,
        selected_functions
    ):
        """
        Plot selected ideal functions.
        """

        output_file(
            self.output_folder
            / "selected_ideal_functions.html"
        )

        plot = figure(
            title="Selected Ideal Functions"
        )

        colors = [
            "blue",
            "red",
            "green",
            "purple"
        ]

        for index, ideal_function in enumerate(
            selected_functions.values()
        ):

            plot.line(
                ideal_df["x"],
                ideal_df[ideal_function],
                color=colors[index],
                legend_label=ideal_function,
                line_width=2
            )

        save(plot)

        self.log(
            "Ideal function plot created"
        )

    def plot_mapping_results(
        self,
        mapped_df
    ):
        """
        Plot mapped test points.
        """

        output_file(
            self.output_folder
            / "test_mapping_results.html"
        )

        plot = figure(
            title="Mapped Test Data"
        )

        plot.scatter(
            mapped_df["x"],
            mapped_df["y"],
            size=8
        )

        save(plot)

        self.log(
            "Mapping plot created"
        )