"""Table."""

# pylint: disable=too-few-public-methods


class Table:
    """Table."""

    def __init__(self, scheme):
        self.scheme = scheme

    def load_variables(self, input_variables=None):
        """Load variables."""
        if input_variables is None:
            return None

        return {
            variable: input_variables[variable]
            for variable in input_variables
            if variable in self.scheme
        }
