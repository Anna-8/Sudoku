import copy
from Sudoku import *
from ForwardChecking import *
from MAC import *


def Backtracking_Search(Sudoku, strategy):
    return (Backtrack({}, Sudoku, strategy))


def Backtrack(assignment, Sudoku, strategy):
    if isComplete(assignment):
        return assignment
    var = Select_Unassigned_Variables(assignment, Sudoku)
    copy_values = copy.deepcopy(Sudoku.values)
    for value in Order_Domain_Values(var, Sudoku):
        if isConsistent(var, value, assignment, Sudoku):
            assignment[var] = value
            inferences = {}
            inferences = Inference(assignment, inferences, Sudoku, var, value, strategy)
            if inferences != "failure":
                result = Backtrack(assignment, Sudoku, strategy)
                if result != "failure":
                    return result
            del assignment[var]
            Sudoku.values.update(copy_values)

    return "failure"


def Inference(assignment, inferences, Sudoku, var, value, strategy):
    if strategy == 0:
        return Forward_Checking(assignment, inferences, Sudoku, var, value)

    else:
        return MAC(assignment, inferences, Sudoku, var, value)


def Print_Result(values):
    for r in rows:
        for c in cols:
            print(values[r + c], ' ', end=' ')
        print(end='\n')


# verifica se tutte le celle sono state riempite
def isComplete(assignment):
    return set(assignment.keys()) == set(squares)


def Select_Unassigned_Variables(assignment, Sudoku):
    unassigned_variables = dict(
        (cells, len(Sudoku.values[cells])) for cells in Sudoku.values if cells not in assignment.keys())
    mrv = min(unassigned_variables, key=unassigned_variables.get)
    return mrv


# restituisce i valori possibili della cella
def Order_Domain_Values(cell, Sudoku):
    return Sudoku.values[cell]


# controlla se l'assegnazione di value a var viola i vincoli
def isConsistent(var, value, assignment, Sudoku):
    for variable in Sudoku.peers[var]:
        if variable in assignment.keys() and assignment[variable] == value:
            return False
    return True


def print_board(board):
    for i in range(81):
        if (i % 9 == 0):
            print(end="\n")
        print(board[i], ' ', end=' ')
    print(end="\n")


