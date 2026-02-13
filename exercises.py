class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")

        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            break  # temporary test

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()

            if move not in self.board:
                print("Invalid move format. Try again.")
                continue

            if self.board[move] is not None:
                print("That space is already taken. Try again.")
                continue

            self.board[move] = self.turn
            break
    def check_winner(self):
        winning_combinations = [
            # Rows
            ('a1', 'b1', 'c1'),
            ('a2', 'b2', 'c2'),
            ('a3', 'b3', 'c3'),

            # Columns
            ('a1', 'a2', 'a3'),
            ('b1', 'b2', 'b3'),
            ('c1', 'c2', 'c3'),

            # Diagonals
            ('a1', 'b2', 'c3'),
            ('c1', 'b2', 'a3')
        ]

        for combo in winning_combinations:
            a, b, c = combo

            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                self.winner = self.board[a]
                return
    def check_tie(self):
        if not self.winner and all(self.board[position] is not None for position in self.board):
            self.tie = True


    def print_board(self):
        b = self.board
        print(f"""
      A   B   C
1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
    ----------
2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
    ----------
3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
""")

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()


game_instance = Game()
game_instance.play_game()
