class Game:
    def __init__(self):
        # Track whose turn it is
        self.turn = 'X'
        
        # Track if the game ended in a tie
        self.tie = False
        
        # Store the winner (None at start)
        self.winner = None
        
        # Create the game board as a dictionary
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
