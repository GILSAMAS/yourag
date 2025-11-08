class CLICommands:
    """
    Factory class for CLI commands.
    """

    __available_commands = {}

    def execute(self, args):
        """
        Execute the command with the given arguments.
        :param args: The command-line arguments.
        """
        raise NotImplementedError("Subclasses must implement this method.")

        """
        Execute the command with the given arguments.
        :param args: The command-line arguments.
        """
        raise NotImplementedError("Subclasses must implement this method.")
