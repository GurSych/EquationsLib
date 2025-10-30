import g_equations as ge
import g_equations.np_handler as ge_np

print(ge.equ_to_dict("x + 72.3y - 3z = 8.0"))
print(ge.dict_to_str(ge.equ_to_dict("x + 72.3y - 3z = 8.0")))
p = ge_np.matrixs_from_equs([
    "3x - y + 2z = -4",
    "x + 4y - z = 10",
    "2x + 3y + z = 8"
])
print(ge_np.matrix_to_str(p[0]))
print(ge_np.matrix_to_str(p[1]))
print(ge_np.numpy_from_equs([
    "3x - y + 2z = -4",
    "x + 4y - z = 10",
    "2x + 3y + z = 8"
]))
print(ge_np.solve_equs([
    "2a+2b-c+d=4",
    "+3b-c+4a+3d=6",
    "12a+5b-3c-4a+4d=12",
    "3a+3b-2c+2d=6"
]))
print(ge.equ_to_dict("3x - y + 2z = -4"))
print(ge.equ_to_dict("x + 4y - z = 10"))
print(ge.equ_to_dict("2x + 3y + z = 8"))
print(ge_np.solve_equs(["x + y = 4","y = 3"],add_values=True))
print(ge_np.roots_of_dicts([{'x':1,'y':1,'res':4},{'y':1,'res':3}],add_values=True))