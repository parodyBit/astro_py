

class LibNova:
    __instance = None

    @staticmethod
    def master():
        """ Static access method. """
        if LibNova.__instance is None:
            LibNova()
        return LibNova.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if LibNova.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            LibNova.__instance = self
