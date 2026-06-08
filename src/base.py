"""
Base component for all project modules.
"""


class BaseComponent:
    """
    Parent class providing common functionality
    to all project components.
    """

    def log(self, message: str) -> None:
        """
        Print a formatted log message.

        Args:
            message (str): Message to display.
        """
        print(f"[INFO] {message}")