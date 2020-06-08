from Backtrack import *
from timeit import default_timer as timer
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def main():
    x = np.arange(0, 25)
    print("EASY SUDOKU")
    f = open("sudokuEasy", "r")
    time_Forwarding = []
    time_MAC = []
    i = 0
    for line in f:
        board = (Convert_String(line))
        sudoku = Sudoku(board)
        start = timer()
        Backtracking_Search(sudoku, 0)
        end = timer()
        print(i, "forwarding", end - start)
        time_Forwarding.append(end - start)
        sudoku = Sudoku(board)
        start = timer()
        Backtracking_Search(sudoku, 1)
        end = timer()
        print(i, "MAC", end - start)
        time_MAC.append(end - start)
        i = i + 1
        del (sudoku)
    f.close()
    f = open("sudokuEasy2", "r")
    for line in f:
        board = (Convert_String(line))
        sudok = Sudoku(board)
        start = timer()
        Backtracking_Search(sudok, 0)
        end = timer()
        print(i, "forwarding", end - start)
        time_Forwarding.append(end - start)
        sudok = Sudoku(board)
        start = timer()
        Backtracking_Search(sudok, 1)
        end = timer()
        print(i, "MAC", end - start)
        time_MAC.append(end - start)
        i = i + 1

    plt.plot(x, time_Forwarding, label="forwarding")
    plt.plot(x, time_MAC, label="MAC")
    plt.ylabel('tempo di risoluzione')
    plt.legend()
    plt.show()

    print("average_Forwarding_easy", np.average(time_Forwarding))
    print("average_MAC_easy ", np.average(time_MAC))

    print("EXPERT SUDOKU")

    f = open("sudokuExpert", "r")
    time_Forwarding = []
    time_MAC = []
    i = 0
    for line in f:
        board = (Convert_String(line))
        sudoku = Sudoku(board)
        start = timer()
        Backtracking_Search(sudoku, 0)
        end = timer()
        print(i, "forwarding", end - start)
        time_Forwarding.append(end - start)
        sudoku = Sudoku(board)
        start = timer()
        Backtracking_Search(sudoku, 1)
        end = timer()
        print(i, "MAC", end - start)
        time_MAC.append(end - start)
        i = i + 1

    plt.plot(x, time_Forwarding, label="forwarding")
    plt.plot(x, time_MAC, label="MAC")
    plt.ylabel('tempo di risoluzione')
    plt.legend()
    plt.show()

    print("average_Forwarding_expert", np.average(time_Forwarding))
    print("average_MAC_expert", np.average(time_MAC))


if __name__ == "__main__":
    main()
