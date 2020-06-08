def Forward_Checking(assignment, inferences, Sudoku, var, value):
    inferences[var] = value
    for variable in Sudoku.peers[var]:
        if variable not in assignment and value in Sudoku.values[variable]:
            if len(Sudoku.values[variable]) == 1:
                return "failure"
            remaining = Sudoku.values[variable].replace(value, "")
            if len(remaining) == 1:
                inf = Forward_Checking(assignment, inferences, Sudoku, variable, remaining)
                if inf == "failure":
                    return "failure"

    return inferences
