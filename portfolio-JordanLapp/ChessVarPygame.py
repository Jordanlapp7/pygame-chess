import pygame
from copy import deepcopy

SIZE = 480
TILE = SIZE / 8
BOARD_POS = (0, 0)


class Piece(pygame.sprite.Sprite):
    def __init__(self, color, type, coordinate_tuple):
        super().__init__()
        self.color = color
        self.type = type
        self.coordinate_tuple = coordinate_tuple

        # Load correct image
        if self.color == 'w':
            if self.type == 'n':
                self.image = pygame.image.load('graphics/Chess_nlt60.png')
            elif self.type == 'b':
                self.image = pygame.image.load('graphics/Chess_blt60.png')
            elif self.type == 'r':
                self.image = pygame.image.load('graphics/Chess_rlt60.png')
            else:
                self.image = pygame.image.load('graphics/Chess_klt60.png')
        else:
            if self.type == 'n':
                self.image = pygame.image.load('graphics/Chess_ndt60.png')
            elif self.type == 'b':
                self.image = pygame.image.load('graphics/Chess_bdt60.png')
            elif self.type == 'r':
                self.image = pygame.image.load('graphics/Chess_rdt60.png')
            else:
                self.image = pygame.image.load('graphics/Chess_kdt60.png')
        self.rect = self.image.get_rect(topleft=(self.coordinate_tuple[0] * TILE, self.coordinate_tuple[1] * TILE))

    def __deepcopy__(self, memo):
        return Piece(self.color, self.type, self.coordinate_tuple)

    def vision(self, board):
        """Takes a board state and returns its possible moves as a list of coordinate tuples"""
        check = False
        x = self.coordinate_tuple[0]
        y = self.coordinate_tuple[1]
        vision = []

        # Knight
        if self.type == 'n':
            vision = [(x - 1, y + 2), (x + 1, y + 2), (x - 2, y + 1), (x + 2, y + 1), (x - 2, y - 1), (x + 2, y - 1),
                      (x - 1, y - 2), (x + 1, y - 2)]
            for coordinate in list(vision):

                # Check space is on board
                if coordinate[0] < 0 or coordinate[0] > 7 or coordinate[1] < 0 or coordinate[1] > 7:
                    vision.remove(coordinate)

                # Check space is not occupied by piece on same team
                elif board[coordinate[1]][coordinate[0]] is not None:
                    if board[coordinate[1]][coordinate[0]].color == self.color:
                        vision.remove(coordinate)
                    # Check space is not occupied by opposing king
                    elif board[coordinate[1]][coordinate[0]].type == 'k':
                        check = True
                        vision.remove(coordinate)

        # Bishop
        elif self.type == 'b':
            # Up and left
            i = 1
            while x - i >= 0 and y - i >= 0:
                if board[y - i][x - i] is None:
                    vision.append((x - i, y - i))
                elif board[y - i][x - i].color == self.color:
                    break
                elif board[y - i][x - i].type == 'k':
                    check = True
                    break
                else:
                    vision.append((x - i, y - i))
                    break
                i += 1

            # Up and right
            i = 1
            while x + i <= 7 and y - i >= 0:
                if board[y - i][x + i] is None:
                    vision.append((x + i, y - i))
                elif board[y - i][x + i].color == self.color:
                    break
                elif board[y - i][x + i].type == 'k':
                    check = True
                    break
                else:
                    vision.append((x + i, y - i))
                    break
                i += 1

            # Down and left
            i = 1
            while x - i >= 0 and y + i <= 7:
                if board[y + i][x - i] is None:
                    vision.append((x - i, y + i))
                elif board[y + i][x - i].color == self.color:
                    break
                elif board[y + i][x - i].type == 'k':
                    check = True
                    break
                else:
                    vision.append((x - i, y + i))
                    break
                i += 1

                # Down and right
            i = 1
            while x + i <= 7 and y + i <= 7:
                if board[y + i][x + i] is None:
                    vision.append((x + i, y + i))
                elif board[y + i][x + i].color == self.color:
                    break
                elif board[y + i][x + i].type == 'k':
                    check = True
                    break
                else:
                    vision.append((x + i, y + i))
                    break
                i += 1

        # Rook
        elif self.type == 'r':
            # Up
            i = 1
            while y - i >= 0:
                if board[y - i][x] is None:
                    vision.append((x, y - i))
                elif board[y - i][x].color == self.color:
                    break
                elif board[y - i][x].type == 'k':
                    check = True
                    break
                else:
                    vision.append((x, y - i))
                    break
                i += 1

            # Right
            i = 1
            while x + i <= 7:
                if board[y][x + i] is None:
                    vision.append((x + i, y))
                elif board[y][x + i].color == self.color:
                    break
                elif board[y][x + i].type == 'k':
                    check = True
                    break
                else:
                    vision.append((x + i, y))
                    break
                i += 1

            # Down
            i = 1
            while y + i <= 7:
                if board[y + i][x] is None:
                    vision.append((x, y + i))
                elif board[y + i][x].color == self.color:
                    break
                elif board[y + i][x].type == 'k':
                    check = True
                    break
                else:
                    vision.append((x, y + i))
                    break
                i += 1

                # Left
            i = 1
            while x - i >= 0:
                if board[y][x - i] is None:
                    vision.append((x - i, y))
                elif board[y][x - i].color == self.color:
                    break
                elif board[y][x - i].type == 'k':
                    check = True
                    break
                else:
                    vision.append((x - i, y))
                    break
                i += 1

                # King
        else:
            vision = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                      (x + 1, y + 1)]
            for coordinate in list(vision):
                # Check space is on board
                if coordinate[0] < 0 or coordinate[0] > 7 or coordinate[1] < 0 or coordinate[1] > 7:
                    vision.remove(coordinate)

                # Check space is not occupied by piece on same team
                elif board[coordinate[1]][coordinate[0]] is not None:
                    if board[coordinate[1]][coordinate[0]].color == self.color:
                        vision.remove(coordinate)
                    # Check space is not occupied by opposing king
                    elif board[coordinate[1]][coordinate[0]].type == 'k':
                        check = True
                        vision.remove(coordinate)

        return vision, check


class Board:
    def __init__(self, default=True):
        self.pieces = pygame.sprite.Group()
        if default:
            self.pieces.add(Piece('w', 'r', (0, 6)))
            self.pieces.add(Piece('w', 'k', (0, 7)))
            self.pieces.add(Piece('w', 'b', (1, 6)))
            self.pieces.add(Piece('w', 'b', (1, 7)))
            self.pieces.add(Piece('w', 'n', (2, 6)))
            self.pieces.add(Piece('w', 'n', (2, 7)))

            self.pieces.add(Piece('b', 'r', (7, 6)))
            self.pieces.add(Piece('b', 'k', (7, 7)))
            self.pieces.add(Piece('b', 'b', (6, 6)))
            self.pieces.add(Piece('b', 'b', (6, 7)))
            self.pieces.add(Piece('b', 'n', (5, 6)))
            self.pieces.add(Piece('b', 'n', (5, 7)))
        self.board = []
        for y in range(8):
            self.board.append([])
            for x in range(8):
                self.board[y].append(None)
        for y in range(8):
            for x in range(8):
                for piece in self.pieces:
                    if (x, y) == piece.coordinate_tuple:
                        self.board[y][x] = piece
        self.game_state = "UNFINISHED"
        self.turn = 'w'
        self.score = 0

    def update_scores(self):
        for piece in self.pieces:
            if piece.color == 'w':
                if piece.type == 'n' or piece.type == 'b':
                    self.score += 3
                elif piece.type == 'r':
                    self.score += 5
                else:
                    if piece.coordinate_tuple[1] == 0:
                        self.score += 1000
                    else:
                        self.score += 50 - piece.coordinate_tuple[1] * 4
            else:
                if piece.type == 'n' or piece.type == 'b':
                    self.score -= 3
                elif piece.type == 'r':
                    self.score -= 5
                else:
                    if piece.coordinate_tuple[1] == 0:
                        self.score -= 1000
                    else:
                        self.score -= 30 - piece.coordinate_tuple[1] * 4

    def update_turn(self):
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'

    def update_game_state(self):
        kings = []
        for top_row in self.board[0]:
            if top_row is not None and top_row.type == 'k':
                kings.append(top_row)
        if len(kings) == 2:
            self.game_state = "TIE"
        elif len(kings) == 1:
            if kings[0].color == 'b':
                self.game_state = "BLACK WINS"
            elif self.turn == 'w':
                self.game_state = "WHITE WINS"
        else:
            self.game_state = "STALEMATE"
            for y in range(8):
                for x in range(8):
                    if self.board[y][x]:
                        vision = self.board[y][x].vision(self.board)
                        if len(vision) != 0:
                            self.game_state = "UNFINISHED"

    def make_move(self, piece, new_coordinate):
        x, y = new_coordinate
        if self.board[y][x]:
            self.pieces.remove(self.board[y][x])
        self.board[piece.coordinate_tuple[1]][piece.coordinate_tuple[0]] = None
        self.board[y][x] = piece
        piece.coordinate_tuple = (x, y)
        self.board[y][x].rect.x = self.board[y][x].coordinate_tuple[0] * TILE
        self.board[y][x].rect.y = self.board[y][x].coordinate_tuple[1] * TILE
        self.update_scores()
        self.update_turn()
        self.update_game_state()

    def make_copy(self):
        copy_board = Board(False)
        for piece in self.pieces:
            copy_piece = deepcopy(piece)
            copy_board.pieces.add(copy_piece)
        copy_board.board = []
        for y in range(8):
            copy_board.board.append([])
            for x in range(8):
                copy_board.board[y].append(None)
        for y in range(8):
            for x in range(8):
                for piece in copy_board.pieces:
                    if (x, y) == piece.coordinate_tuple:
                        copy_board.board[y][x] = piece
        copy_board.turn = deepcopy(self.turn)
        copy_board.game_state = deepcopy(self.game_state)
        copy_board.update_scores()
        return copy_board


def create_board_surf():
    board_surf = pygame.Surface((TILE*8, TILE*8))
    dark = False
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x*TILE, y*TILE, TILE, TILE)
            pygame.draw.rect(board_surf, pygame.Color((119, 153, 84) if dark else (233,237,204)), rect)
            dark = not dark
        dark = not dark
    return board_surf


def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
    x, y = [int(v // TILE) for v in mouse_pos]
    try:
        if x >= 0 and y >= 0: return (board[y][x], x, y)
    except IndexError: pass
    return None, None, None


def draw_selector(screen, piece, x, y, turn):
    if piece is not None and piece.color == turn:
        rect = (BOARD_POS[0] + x * TILE, BOARD_POS[1] + y * TILE, TILE, TILE)
        pygame.draw.rect(screen, (244,246,128,50), rect, 2)


def not_in_check(board, piece, end_coordinates):
    end_x, end_y = end_coordinates
    test = [row[:] for row in board]
    test_piece = Piece(piece.color, piece.type, (end_x, end_y))
    test[end_y][end_x] = test_piece
    test[piece.coordinate_tuple[1]][piece.coordinate_tuple[0]] = None
    _, check = test[end_y][end_x].vision(test)
    if check:
        return False
    for row in test:
        for col in row:
            if col is not None:
                _, other_checks = col.vision(test)
                if other_checks:
                    return False
    board = test
    return board


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.game_state != "UNFINISHED":
        return board
    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for y in range(8):
            for x in range(8):
                if board.board[y][x] and board.board[y][x].color == board.turn:
                    moves = board.board[y][x].vision(board.board)
                    for move in moves[0]:
                        test_board = board.make_copy()
                        if not_in_check(test_board.board, test_board.board[y][x], move):
                            test_board.make_move(test_board.board[y][x], move)
                            eval = minimax(test_board, depth - 1, alpha, beta, False)
                            if eval.score >= max_eval:
                                max_eval = eval.score
                                best_move = test_board
                            alpha = max(alpha, eval.score)
                            if beta <= alpha:
                                break
        return best_move
    else:
        min_eval = float('inf')
        for y in range(8):
            for x in range(8):
                if board.board[y][x] and board.board[y][x].color == board.turn:
                    moves = board.board[y][x].vision(board.board)
                    for move in moves[0]:
                        test_board = board.make_copy()
                        if not_in_check(test_board.board, test_board.board[y][x], move):
                            test_board.make_move(test_board.board[y][x], move)
                            eval = minimax(test_board, depth - 1, alpha, beta, True)
                            if eval.score <= min_eval:
                                min_eval = eval.score
                                best_move = test_board
                            beta = min(beta, eval.score)
                            if beta <= alpha:
                                break
        return best_move


def main():
    pygame.init()
    screen = pygame.display.set_mode((SIZE - 1, SIZE - 1))
    pygame.display.set_caption('Chess Racer')
    clock = pygame.time.Clock()
    board_surf = create_board_surf()
    board_object = Board()

    pygame.font.init()
    my_font = pygame.font.SysFont('verdana', 30)
    w_text = my_font.render("WHITE WINS", True, (255, 255, 255))
    w_text_rect = w_text.get_rect(center=(SIZE/2, SIZE/2 - 40))
    b_text = my_font.render("BLACK WINS", True, (255, 255, 255))
    b_text_rect = b_text.get_rect(center=(SIZE / 2, SIZE / 2 - 40))
    t_text = my_font.render("TIE", True, (255, 255, 255))
    t_text_rect = t_text.get_rect(center=(SIZE / 2, SIZE / 2 - 40))
    s_text = my_font.render("STALEMATE", True, (255, 255, 255))
    s_text_rect = t_text.get_rect(center=(SIZE / 2, SIZE / 2 - 40))
    replay_text = my_font.render("REPLAY", True, (255, 255, 255))
    replay_text_rect = replay_text.get_rect(center=(SIZE / 2, SIZE / 2 + 35))
    end_surf = pygame.Surface((225,150))
    end_surf.fill((38, 36, 33))
    end_surf_rect = end_surf.get_rect(center=((SIZE/2, SIZE/2)))
    restart_surf = pygame.Surface((175, 50))
    restart_surf_rect = restart_surf.get_rect(center=((SIZE/2, SIZE/2 + 35)))

    clicked = False
    selected = False
    selected_piece = None

    while True:
        piece, x, y = get_square_under_mouse(board_object.board)

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and piece and piece.color == board_object.turn and not selected and board_object.game_state == "UNFINISHED":
                selected = True
                selected_piece = piece
                vision = selected_piece.vision(board_object.board)
            if e.type == pygame.MOUSEBUTTONUP and e.button == 1 and selected:
                selected = False
                if (x, y) in vision[0] and not_in_check(board_object.board, selected_piece, (x, y)):
                    board_object.make_move(selected_piece, (x, y))
                selected_piece.rect.x = selected_piece.coordinate_tuple[0] * TILE
                selected_piece.rect.y = selected_piece.coordinate_tuple[1] * TILE

        if board_object.turn == 'b':
            board_object = minimax(board_object, 2, float('-inf'), float('inf'), False)

        if selected:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            selected_piece.rect.center = (mouse_x, mouse_y)

        screen.fill(pygame.Color('gray'))
        screen.blit(board_surf, BOARD_POS)
        if board_object.game_state == "UNFINISHED":
            draw_selector(screen, piece, x, y, board_object.turn)

        board_object.pieces.draw(screen)

        if board_object.game_state != "UNFINISHED":
            screen.blit(end_surf, end_surf_rect)
            screen.blit(restart_surf, restart_surf_rect)
            screen.blit(replay_text, replay_text_rect)
            if board_object.game_state == "WHITE WINS":
                screen.blit(w_text, w_text_rect)
            elif board_object.game_state == "BLACK WINS":
                screen.blit(b_text, b_text_rect)
            elif board_object.game_state == "TIE":
                screen.blit(t_text, t_text_rect)
            elif board_object.game_state == "STALEMATE":
                screen.blit(s_text, s_text_rect)
            mouse_pos = pygame.mouse.get_pos()
            if restart_surf_rect.collidepoint(mouse_pos):
                restart_surf.fill((105, 102, 101))
                if pygame.mouse.get_pressed() == (True, False, False):
                    clicked = True
                    restart_surf.fill((135, 132, 131))
                else:
                    if clicked:
                        clicked = False
                        board_object = Board()
            else:
                clicked = False
                restart_surf.fill((75, 72, 71))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
