import numpy
import typing
import g_equations

class matrix_add_values_kwargs(typing.TypedDict,total=False):
    add_values: bool

def numpy_from_dicts(equations_dicts: list, **kwargs: matrix_add_values_kwargs) -> dict:
    matrix_triple = matrixs_from_dicts(equations_dicts,**kwargs)
    vars          = matrix_triple[2]
    A_matrix      = numpy.matrix(matrix_triple[0])
    B_matrix      = numpy.matrix(matrix_triple[1])
    A1_matrix     = numpy.linalg.inv(A_matrix)
    ans_matrix    = A1_matrix * B_matrix
    var_dict      = dict()
    for i in range(len(vars)):
        var_dict[vars[i]] = float(ans_matrix[i,0])
    return var_dict

def matrixs_from_dicts(equations_dicts: list, **kwargs: matrix_add_values_kwargs) -> tuple:
    allowed_kwargs = {"add_values"}
    for key in kwargs:
        if key not in allowed_kwargs:
            raise Exception("g_equations: Invalid kw-argument: {}".format(key))
    add_values = kwargs.get("add_values",False)
    if add_values:
        keys = set()
        for dict in equations_dicts:
            for key in dict:
                if key not in keys: keys.add(key)
        keys = sorted(keys)
        keys.remove("res")
    else:
        if not all(equations_dicts[i-1].keys() == equations_dicts[i].keys() for i in range(1,len(equations_dicts))):
            raise Exception("g_equations: Equations must have the same variables")
        keys = sorted(equations_dicts[0].keys())
        keys.remove("res")
    if len(keys) != len(equations_dicts):
        raise Exception("g_equations: Number of equations must be equal to number of variables")
    if add_values:
        A_matrix = [list(map(lambda key: e_d[key] if key in e_d.keys() else 0.0, keys)) for e_d in equations_dicts]
    else:
        A_matrix = [list(map(lambda key: e_d[key],keys)) for e_d in equations_dicts]
    B_matrix = [[e_d["res"]] for e_d in equations_dicts]
    return (A_matrix, B_matrix, tuple(keys))

def numpy_from_equs(equations_strs: list, **kwargs: matrix_add_values_kwargs) -> dict:
    return numpy_from_dicts(list(map(g_equations.equ_to_dict,equations_strs)),**kwargs)

roots_of_dicts = numpy_from_dicts
solve_equs     = numpy_from_equs

def matrixs_from_equs(equations_strs: list, **kwargs: matrix_add_values_kwargs) -> list:
    return matrixs_from_dicts(list(map(g_equations.equ_to_dict,equations_strs)),**kwargs)

def matrix_to_str(matrix: list) -> str:
    sttr = ""
    for line in matrix:
        line_str = ""
        for elem in line:
            line_str += ' ' + str(elem)
        sttr += line_str[1:] + "; "
    return sttr[:-2]