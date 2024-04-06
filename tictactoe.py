"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_empty = 0
    for row in board:
        num_empty += row.count(EMPTY)
    if num_empty == 0:
        return None
    elif num_empty % 2 != 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    if terminal(board):
        return None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # make a copy of board
    state = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    # if action is not valid, raise exception
    if state[i][j] is not EMPTY:
        raise Exception("Not a valid action")
    state[i][j] = player(state)
    return state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wins = [[X, X, X], [O, O, O]]
    # check rows
    for i in range(3):
        if board[i] in wins:
            return board[i][0]
    # check columns
        col = []
        for j in range(3):
            col.append(board[j][i])
        if col in wins:
            return board[0][i]
    # check diagonals
    if [board[0][0], board[1][1], board[2][2]] in wins:
        return board[0][0]
    elif [board[0][2], board[1][1], board[2][0]] in wins:
        return board[0][2]
    # no win
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        utilities = ["O", None, "X"]
        wnr = winner(board)
        return utilities.index(wnr) - 1
    else:
        raise Exception("Cannot calculate utility for non-terminal board")


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        return maximize(board)[1]
    else:
        return minimize(board)[1]

def minimize(board, alpha=float("-inf")):
    if terminal(board):
        return utility(board), None
    value = float("inf")
    optimal_action = None
    for action in actions(board):
        if alpha >= value:
            break
        v, a = maximize(result(board, action), value)
        if v < value:
            optimal_action = action
            value = v
    return value, optimal_action

def maximize(board, beta=float("inf")):
    if terminal(board):
        return utility(board), None
    value = float("-inf")
    optimal_action = None
    for action in actions(board):
        if beta <= value:
            break
        v, a = minimize(result(board, action), value)
        if v > value:
            optimal_action = action
            value = v
    return value, optimal_action
