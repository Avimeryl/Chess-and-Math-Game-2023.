import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move
from MathQuiz import MathQuizGUI
WHITE = "white"
BLACK = "black"
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
        # Modification code to create time
        self.clock = pygame.time.Clock()
        self.white_time = 600000
        self.black_time = 610000
        self.current_player = WHITE
        self.font = pygame.font.Font(None, 28)

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # show methods
            self.clock.tick(60)
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)
            if self.current_player == WHITE:
                self.white_time -= self.clock.get_time()
            else:
                self.black_time -= self.clock.get_time()

            # Check if time has run out for the current player
            if self.current_player == WHITE and self.white_time <= 0:
                print("White player ran out of time!")
                # Handle time out for the white player
            elif self.current_player == BLACK and self.black_time <= 0:
                print("Black player ran out of time!")
            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    # if clicked square has a piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece (color) ?
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                # click release
                elif event.type == pygame.MOUSEBUTTONUP:

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # valid move ?
                        if board.valid_move(dragger.piece, move):
                            self.quiz = MathQuizGUI()
                            # normal capture
                            captured = board.squares[released_row][released_col].has_piece()
                               
                            if not self.quiz.run():
                                print("Wrong answer!")
                                # Handle the wrong answer here, such as showing an error message or resetting the game
                            else:
                                board.move(dragger.piece, move)
                                board.set_true_en_passant(dragger.piece)     
                                # sounds
                                game.play_sound(captured)
                                # show methods
                                game.show_bg(screen)
                                game.show_last_move(screen)
                                game.show_pieces(screen)


                                # next turn
                            #game.next_turn()
                            self.current_player = game.next_turn()

                    dragger.undrag_piece()

                # key press
                elif event.type == pygame.KEYDOWN:

                    # changing themes
                    if event.key == pygame.K_t:
                        game.change_theme()

                    # reset the game
                    if event.key == pygame.K_r:
                        game.reset()
                        self.white_time = 600000
                        self.black_time = 600000
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

                # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            black_timer_text = self.font.render("Black: {:.2f}".format(self.black_time / 1000), True, (255, 255, 255))
            white_timer_text = self.font.render("White: {:.2f}".format(self.white_time / 1000), True, (255, 255, 255))

            timer_background = pygame.Surface((200, 60))
            timer_background.fill((0, 0, 0))
            timer_background.set_alpha(128)
            self.screen.blit(timer_background, (10, 10))  # Adjust the position as needed
            self.screen.blit(black_timer_text, (20, 20))  # Adjust the position as needed 
            self.screen.blit(white_timer_text, (20, 50))  # Adjust the position as needed
            
            pygame.display.update()
            self.current_player = self.game.next_player


main = Main()
main.mainloop()
