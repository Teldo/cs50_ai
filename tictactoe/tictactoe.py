"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math
import time

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
    if board == initial_state():
        return X
    else:
        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    x_count += 1
                elif board[i][j] == O:
                    o_count += 1
        if x_count > o_count:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """    
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")
    result = deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # check columns
        elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        # check diagonals
        elif board[0][0] == board[1][1] == board[2][2] != EMPTY:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
            return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
        if v == 1:
            return v
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
        if v == -1:
            return v
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # measure runtime in ms
    start = time.time()
    if terminal(board):
        return None
    if player(board) == X:
        if board == initial_state():
            return (1,1)
        value = max_value(board)
        for action in actions(board):
            if value == min_value(result(board, action)):
                end = time.time()
                print("Runtime: ", (end - start) * 1000, "ms")
                print("Value: ", value)
                return action
    else:
        value = min_value(board)
        for action in actions(board):
            if value == max_value(result(board, action)):
                end = time.time()
                print("Runtime: ", (end - start) * 1000, "ms")
                print("Value: ", value)
                return action
    