"""Interactor for creating a new game of Tic Tac Toe."""
from App.UseCase_Interactors.CreateGame import CGInputData, CGOutputData
from Entities import Game
from Entities.Board import Board
from Entities.Player import Player


class CreateInteractor:
    """Interactor for creating a new game."""

    def __init__(self, input_data: CGInputData) -> None:
        """holds the input data and creates a new game accordingly"""
        self.rows = input_data.board_row
        self.columns = input_data.board_column
        self.player1 = (input_data.player1type, input_data.player1name, input_data.player1symbol)
        self.player2 = (input_data.player2type, input_data.player2name, input_data.player2symbol)

    def create_new_game_output(self) -> CGOutputData:
        """Creates a new game from the input data. Transforms and returns basic data to output data
        """
        new_board = Board(self.rows, self.columns)
        board_dict_map = new_board.the_board
        final_output_data = CGOutputData.CGOutputData(board_dict_map, self.player1[1],
                                                      self.player2[1], self.player1[0],
                                                      self.player2[0], self.player1[2],
                                                      self.player2[2])
        return final_output_data

    def create_new_game_repo(self) -> Game:
        """Creates a new game from the input data. Returns the game state (board, game, and player)
        to the game_repository in the DataAccessLayer."""
        new_board = Board(self.rows, self.columns)
        player1 = Player(self.player1[1], self.player1[2])
        player2 = Player(self.player2[1], self.player2[2])
        new_game = Game.Game(player1, player2, new_board)
        return new_game
