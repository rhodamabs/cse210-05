class Credit:
    """
    An update that displays the game contibutors when the game is over.
    
    The responsibility of Credit is to display the team that contributed to the game.
    """

    def __init__(self):
        """Constructs a new instance of Credit.
        """
        self._name = "Rhoda Mabundu"

        pass

    def getCredits(self):
        """Sets the contributors flag below game over flag if the snake collides with one of its own segments (game over).
        """
        return f"Updated by: {self._name}"
        


        