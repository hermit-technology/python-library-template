class DomainLogic:
    """
    A class to provide some example logic and functionality for a python library.
    """

    def __init__(self) -> None:
        """
        Constructs a DomainLogic class.
        """

    def do_hello(self, name: str = None) -> None:
        """
        Prints a hello message.

        :param str name: (Optional) A name to say hello to. If no name is provided, we say hi to the world instead.
        """
        name = "World" if name == None else name
        print(f"Hello {name}!")
