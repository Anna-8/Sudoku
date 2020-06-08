from queue import Queue


def MAC(assignment, inferences, Sudoku, var, value):
    inferences[var] = value
    q = Queue()
    for (Xj,Xi) in Sudoku.constraints:
        if Xj not in assignment and Xi == var:
            q.put((Xj, Xi))

    while not q.empty():
        (Xj, Xi) = q.get()
        if REVISE(Sudoku, Xi, Xj):
            if len(Sudoku.values[Xi]) == 0:
                return "failure"
            for Xk in Sudoku.peers[Xi]:
                if Xk != Xj:
                    q.put((Xk, Xi))
    return inferences


def REVISE(Sudoku, Xj, Xi):
    revised = False
    for value in set(Sudoku.values[Xj]):
        if not Consistent(Sudoku, value, Xj, Xi):
            Sudoku.values[Xi].replace(value, "")
            revised = True
    return revised


def Consistent(Sudoku, value, Xi, Xj):
    for v in Sudoku.values[Xj]:
        if Xj in Sudoku.peers[Xi] and v != value:
            return True

    return False


