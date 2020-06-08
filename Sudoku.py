domain = cols = "123456789"
rows = "ABCDEFGHI"


def Convert_String(board=""):
    string = ""
    for i in range(len(board)):
        if board[i] != ".":
            string = string + board[i]
        else:
            string = string + "0"
    return string


def cross(A, B):
    return [a + b for a in A for b in B]


squares = cross(rows, cols)


class Sudoku:
    def __init__(self, board=""):

        self.variables = cross(rows, cols)
        self.domain = self.Build_Dict(board)
        self.values = self.Build_Dict(board)

        # costruzione dei 27 gruppi di variabili vincolate:
        self.unitlist = ([cross(rows, c) for c in cols] +
                         [cross(r, cols) for r in rows] +
                         [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

        # a ogni cella si associano i gruppi di vincoli a cui appartiene
        self.units = dict((s, [u for u in self.unitlist if s in u])
                          for s in squares)
        # a ogni cella si associa un'unica lista con tutte le variabili con cui è vincolata
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s]))
                          for s in squares)
        self.constraints = {(variable, peer) for variable in self.variables for peer in self.peers[variable]}

    # costruisce un dizionario che associa a ogni cella del sudoku i valori che essa può assumere
    def Build_Dict(self, board=""):
        values = dict()
        k = 0
        for variable in self.variables:
            if board[k] != "0":
                values[variable] = board[k]
            else:
                values[variable] = domain
            k = k + 1
        return values
