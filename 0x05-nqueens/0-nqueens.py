#!/usr/bin/python3
""" a program that solves the N queens problem"""
import sys


def chess_board(n):
    """initialize an `n`x`n` sized chessboard with 0's"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def chess_deepcopy(board):
    """return a deepcopy of the chessboard"""
    if isinstance(board, list):
        return list(map(chess_deepcopy, board))
    return (board)


def get_solve(board):
    """return a list of lists representation of the solved chessboard"""
    solved = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solved.append([row, col])
                break
    return (solved)


def x_isout(board, row, col):
    """X out spots on a chessboard
        all the spots where non-attacking queens can no
        longer be played are X-ed out
    Args:
        board (list): is the current working chessboard
        row (int): is the row where a queen was last played
        col (int): is the column where a queen was last played
    """
    # X out all the forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all the backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all the spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all the spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all the spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all the spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all the spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all the spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """solve an N-queens puzzle recursively
    Args:
        board (list): is the current working chessboard
        row (int): is the current working row
        queens (int): is the current number of placed queens
        solutions (list): is a list of lists of solutions
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solve(board))
        return (solutions)

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = chess_deepcopy(board)
            tmp_board[row][col] = "Q"
            x_isout(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = chess_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
