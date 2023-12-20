# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 8/17/2023
# Description: Creates a chess variant with the goal of moving your king to the top row.

class Piece:
    """A piece that is on the board"""
    def __init__(self, color, type, coordinate_tuple):
        self._color = color
        self._type = type
        self._coordinate_tuple = coordinate_tuple

    def get_color(self):
        """Returns piece color"""
        return self._color

    def get_type(self):
        """Returns piece type"""
        return self._type
    
    def get_coordinate_tuple(self):
        """Returns piece coordinates as a tuple"""

    def vision(self, board):
        """Takes a board state and returns its possible moves as a list of coordinate tuples"""
        check = False
        x = self._coordinate_tuple[0]
        y = self._coordinate_tuple[1]
        vision = []

        # Knight
        if self._type == 'n':
            vision = [(x-1, y+2), (x+1, y+2), (x-2, y+1), (x+2, y+1), (x-2, y-1), (x+2, y-1), (x-1, y-2), (x+1, y-2)]
            for coordinate in list(vision):

                # Check space is on board
                if coordinate[0] < 0 or coordinate[0] > 7 or coordinate[1] < 0 or coordinate[1] > 7:
                    vision.remove(coordinate)

                # Check space is not occupied by piece on same team
                elif board[coordinate[1]][coordinate[0]] is not None:
                    if board[coordinate[1]][coordinate[0]].get_color() == self._color:
                        vision.remove(coordinate)
                    # Check space is not occupied by opposing king
                    elif board[coordinate[1]][coordinate[0]].get_type() == 'k':
                        check = True
                        vision.remove(coordinate)
        
        # Bishop
        elif self._type == 'b':
            # Up and left
            i = 1
            while x-i >= 0 and y-i >= 0:
                if board[y-i][x-i] is None:
                    vision.append((x-i, y-i))
                elif board[y-i][x-i].get_color() == self._color:
                    break
                elif board[y-i][x-i].get_type() == 'k':
                    check = True
                    break
                else:
                    vision.append((x-i, y-i))
                    break
                i += 1

            # Up and right
            i = 1
            while x+i <= 7 and y-i >= 0:
                if board[y-i][x+i] is None:
                    vision.append((x+i, y-i))
                elif board[y-i][x+i].get_color() == self._color:
                    break
                elif board[y-i][x+i].get_type() == 'k':
                    check = True
                    break
                else:
                    vision.append((x+i, y-i))
                    break
                i += 1

            # Down and left
            i = 1
            while x-i >= 0 and y+i <= 7:
                if board[y+i][x-i] is None:
                    vision.append((x-i, y+i))
                elif board[y+i][x-i].get_color() == self._color:
                    break
                elif board[y+i][x-i].get_type() == 'k':
                    check = True
                    break
                else:
                    vision.append((x-i, y+i))
                    break
                i += 1

                # Down and right
            i = 1
            while x+i <= 7 and y+i <= 7:
                if board[y+i][x+i] is None:
                    vision.append((x+i, y+i))
                elif board[y+i][x+i].get_color() == self._color:
                    break
                elif board[y+i][x+i].get_type() == 'k':
                    check = True
                    break
                else:
                    vision.append((x+i, y+i))
                    break
                i += 1

        # Rook
        elif self._type == 'r':
            # Up
            i = 1
            while y-i >= 0:
                if board[y-i][x] is None:
                    vision.append((x, y-i))
                elif board[y-i][x].get_color() == self._color:
                    break
                elif board[y-i][x].get_type() == 'k':
                    check = True
                    break
                else:
                    vision.append((x, y-i))
                    break
                i += 1

            # Right
            i = 1
            while x+i <= 7:
                if board[y][x+i] is None:
                    vision.append((x+i, y))
                elif board[y][x+i].get_color() == self._color:
                    break
                elif board[y][x+i].get_type() == 'k':
                    check = True
                    break
                else:
                    vision.append((x+i, y))
                    break
                i += 1

            # Down
            i = 1
            while y+i <= 7:
                if board[y+i][x] is None:
                    vision.append((x, y+i))
                elif board[y+i][x].get_color() == self._color:
                    break
                elif board[y+i][x].get_type() == 'k':
                    check = True
                    break
                else:
                    vision.append((x, y+i))
                    break
                i += 1

                # Left
            i = 1
            while x-i >= 0:
                if board[y][x-i] is None:
                    vision.append((x-i, y))
                elif board[y][x-i].get_color() == self._color:
                    break
                elif board[y][x-i].get_type() == 'k':
                    check = True
                    break
                else:
                    vision.append((x-i, y))
                    break
                i += 1    

            # King
        else:
            vision = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
            for coordinate in list(vision):
                # Check space is on board
                if coordinate[0] < 0 or coordinate[0] > 7 or coordinate[1] < 0 or coordinate[1] > 7:
                    vision.remove(coordinate)

                # Check space is not occupied by piece on same team
                elif board[coordinate[1]][coordinate[0]] is not None:
                    if board[coordinate[1]][coordinate[0]].get_color() == self._color:
                        vision.remove(coordinate)
                    # Check space is not occupied by opposing king
                    elif board[coordinate[1]][coordinate[0]].get_type() == 'k':
                        check = True
                        vision.remove(coordinate)
        return vision, check


class ChessVar:
    """Creates a game of a chess variant; includes move and game state methods."""
    def __init__(self):
        self._game_state = "UNFINISHED"
        self._turn = 'w'

        # Make empty board
        self._board = [[None for i in range(8)] for i in range(8)]

        # Place white pieces
        self._board[6][0] = Piece('w', 'r', (0, 6))
        self._board[7][0] = Piece('w', 'k', (0, 7))
        self._board[6][1] = Piece('w', 'b', (1, 6))
        self._board[7][1] = Piece('w', 'b', (1, 7))
        self._board[6][2] = Piece('w', 'n', (2, 6))
        self._board[7][2] = Piece('w', 'n', (2, 7))

        # Place black pieces
        self._board[6][7] = Piece('b', 'r', (7, 6))
        self._board[7][7] = Piece('b', 'k', (7, 7))
        self._board[6][6] = Piece('b', 'b', (6, 6))
        self._board[7][6] = Piece('b', 'b', (6, 7))
        self._board[6][5] = Piece('b', 'n', (5, 6))
        self._board[7][5] = Piece('b', 'n', (5, 7))

    def get_game_state(self):
        """Returns game state"""
        return self._game_state

    def visualize_board(self):
        """Prints current board state"""
        for row in self._board:
            for col in row:
                if col is None:
                    print('x', end='')
                else:
                    print(col.get_type(), end='')
            print('')

    def change_turn(self):
        """Switches whose turn it is"""
        if self._turn == 'w':
            self._turn = 'b'
        else:
            self._turn = 'w'

    def check_game_state(self):
        """Checks if any end conditions are met"""
        kings = []
        for top_row in self._board[0]:
            if top_row is not None and top_row.get_type() == 'k':
                kings.append(top_row)
        if len(kings) == 2:
            self._game_state = "TIE"
        elif len(kings) == 1:
            if kings[0].get_color() == 'b':
                self._game_state = "BLACK WINS"
            elif self._turn == 'w':
                    self._game_state = "WHITE WINS"            

    def get_piece(self, coordinate_tuple):
        """Returns piece on specified coordinate, or None if empty"""
        return self._board[coordinate_tuple[1]][coordinate_tuple[0]]

    def make_move(self, start, end):
        """Moves a piece from start to end if valid"""
        # Check game is unfinished
        if self._game_state != "UNFINISHED":
            print("Error: Game has already ended!")
            return False

        # Check starting coordinate is on the board
        start_lower = start.lower()
        start_x = ord(start_lower[0]) - 97
        start_y = 7 - (int(start_lower[1]) - 1)
        start_coord = (start_x, start_y)
        if start_x < 0 or start_x > 7 or start_y < 0 or start_y > 7:
            print("Error: Starting coordinate is not on the board!")
            return False

        # Check ending coordinate is on the board
        end_lower = end.lower()
        end_x = ord(end_lower[0]) - 97
        end_y = 7 - (int(end_lower[1]) - 1)
        end_coord = (end_x, end_y)
        if end_x < 0 or end_x > 7 or end_y < 0 or end_y > 7:
            print("Error: Ending coordinate is not on the board!")
            return False

        piece = self._board[start_coord[1]][start_coord[0]]
        # Check piece is on the starting coordinate
        if piece is None:
            print("Error: Starting coordinate has no piece!")
            return False

        # Check piece is on right team
        if piece.get_color() != self._turn:
            print("Error: It is not your turn!")
            return False

        # Check target coordinate is in pieces vision
        vision, _ = piece.vision(self._board)
        if end_coord not in vision:
            print("Error: End coordinate is not a valid space for this piece!")
            return False
        
        # See if move places king in check
        test = [row[:] for row in self._board]
        color = piece.get_color()
        type = piece.get_type()
        test_piece = Piece(color, type, (end_x, end_y))
        test[end_y][end_x] = test_piece
        test[start_y][start_x] = None
        _, check = test[end_y][end_x].vision(test)
        if check == True:
            print("Error: Move places king in check!")
            return False
        for row in test:
            for col in row:
                if col is not None and (col.get_type() == 'b' or col.get_type() == 'r'):
                    _, other_checks = col.vision(test)
                    if other_checks == True:
                        print("Error: Move places king in check!")
                        return False
        self._board = test
        self.change_turn()
        self.check_game_state()
        return True
