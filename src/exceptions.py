"""
Custom exceptions used throughout the project.
"""


class DataLoadError(Exception):
    """Raised when data loading fails."""


class DatabaseError(Exception):
    """Raised when database operations fail."""


class FunctionSelectionError(Exception):
    """Raised when ideal function selection fails."""


class MappingError(Exception):
    """Raised when test data mapping fails."""