import numpy
import g_equations

def numpy_from_dicts(equations_dicts: list) -> dict:
    matrix_pair = matrixs_from_dicts(equations_dicts)
    vars        = sorted(equations_dicts[0].keys())
    vars.remove("res")
    A_matrix   = numpy.matrix(matrix_pair[0])
    B_matrix   = numpy.matrix(matrix_pair[1])
    A1_matrix  = numpy.linalg.inv(A_matrix)
    ans_matrix = A1_matrix * B_matrix
    var_dict   = dict()
    for i in range(len(vars)):
        var_dict[vars[i]] = float(ans_matrix[i,0])
    return var_dict

def matrixs_from_dicts(equations_dicts: list) -> list:
    if len(equations_dicts) < 2:
        raise Exception("g_equations: Module can't calculate it (check for updates)")
    if not all(equations_dicts[i-1].keys() == equations_dicts[i].keys() for i in range(2,len(equations_dicts))):
        raise Exception("g_equations: Equations must have the same variables")
    keys = sorted(equations_dicts[0].keys())
    keys.remove("res")
    if len(keys) != len(equations_dicts):
        raise Exception("g_equations: Number of equations must be equal to number of variables")
    A_matrix = [list(map(lambda key: e_d[key],keys)) for e_d in equations_dicts]
    B_matrix = [[e_d["res"]] for e_d in equations_dicts]
    return [A_matrix, B_matrix]

def numpy_from_equs(equations_strs: list) -> dict:
    return numpy_from_dicts(list(map(g_equations.equ_to_dict,equations_strs)))

roots_of_dicts = numpy_from_dicts
solve_equs     = numpy_from_equs

def matrixs_from_equs(equations_strs: list) -> list:
    return matrixs_from_dicts(list(map(g_equations.equ_to_dict,equations_strs)))

def matrix_to_str(matrix: list) -> str:
    sttr = ""
    for line in matrix:
        line_str = ""
        for elem in line:
            line_str += ' ' + str(elem)
        sttr += line_str[1:] + "; "
    return sttr[:-2]