# g_equations

g_equations is my Python module for working with equations (some things are powered by NumPy)

> _Special thanks to Nastya for her helpful support ^^_

# Using Library

> The library is in development so this section is updated together with library itself

## Library connection

```py
import g_equations
import g_equations.np_handler
```

**Package Requirements:** Some functions from g_equations.np_handler module require NumPy

## Linear equation to dictionary

g_equations module has equ_to_dict(_equation_) function that gets an `str` object with human-like written liner equation and returnes a dictionary with variablies' coefficients

```py
equ_dict = g_equations.equ_to_dict("x + 72.3y - 3z = 8.0")
print(equ_dict) # {'res': 8.0, 'x': 1.0, 'y': 72.3, 'z': -3.0}
equ_dict = g_equations.equ_to_dict("x + 72.3y - 3z - 6 = 8.0 - x")
print(equ_dict) # {'res': 14.0, 'x': 2.0, 'y': 72.3, 'z': -3.0}
```

String should have two parts with `=` between them. All variables are moved to the left side and free terms are moved to the right one<br>
Returned dictionary will have right side value by `"res"` key and variablies' coefficients by their names

> [!WARNING]
> The function works only with variables whose names consist of a single Latin alphabet character

## Linear equation to matrixs

g_equations.np_handler has matrixs_from_dicts(_dictionaries_) function that gets a list of dictionaties (like in [&#39;the section upper&#39;](#linear-equation-to-dictionary)) with variablies' coefficients from a system of equations and returnes list with two entries: matrix of variablies' coefficients and matrix with right side values

> [!NOTE]
> Matrix (not a numpy.matrix) is a list of lists with a rectangular shape<br>
> Like this: `[ [a11,a12,a13], [a21,a22,a23], [a31,a32,a33] ]`

Let's take a look at this system of equations:<br>
$3x - y + 2z = -4;$<br>
$x + 4y - z = 10;$<br>
$2x + 3y + z = 8;$<br>
<br>
Matrix can be got via matrixs_from_dicts(_dictionaries_) like this:

```py
equ1 = {'res': -4.0, 'x': 3.0, 'y': -1.0, 'z': 2.0}
equ2 = {'res': 10.0, 'x': 1.0, 'y':  4.0, 'z': -1.0}
equ3 = {'res':  8.0, 'x': 2.0, 'y':  3.0, 'z': 1.0}
matrix_pair = g_equations.np_handler.matrixs_from_dicts([equ1,equ2,equ3])
```

There is also matrixs_from_equs(_equations_) function that gets a list of `str` objects with [&#39;human-like written liner equations&#39;](#linear-equation-to-dictionary) and do the same things as matrixs_from_dicts(_dictionaries_)

```py
matrix_pair = g_equations.np_handler.matrixs_from_equs([
    "3x - y + 2z = -4",
    "x + 4y - z = 10",
    "2x + 3y + z = 8"
])
```

Both `matrix_pair` look like:

```
matrix_pair[0]: [ [3.0,-1.0, 2.0],        matrix_pair[1]: [ [-4.0],
                  [1.0, 4.0,-1.0],                          [10.0],
                  [2.0, 3.0, 1.0] ]                         [ 8.0] ]      
```

## Solve system of linear equations

g_equations.np_handler has numpy_from_dicts(_dictionaries_) function that gets a list of dictionaties (like in [&#39;the section upper&#39;](#linear-equation-to-dictionary)) with variablies' coefficients from a system of equations and returnes dictionary with system's roots: roots' coefficients by names of their variables

Let's take a look at this system of equations:<br>
$3x - y + 2z = -4;$<br>
$x + 4y - z = 10;$<br>
$2x + 3y + z = 8;$<br>
<br>
Roots can be got via numpy_from_dicts(_dictionaries_) like this:

```py
equ1 = {'res': -4.0, 'x': 3.0, 'y': -1.0, 'z': 2.0}
equ2 = {'res': 10.0, 'x': 1.0, 'y':  4.0, 'z': -1.0}
equ3 = {'res':  8.0, 'x': 2.0, 'y':  3.0, 'z': 1.0}
system_roots = g_equations.np_handler.numpy_from_dicts([equ1,equ2,equ3])
```

There is also numpy_from_equs(_equations_) function that gets a list of `str` objects with [&#39;human-like written liner equations&#39;](#linear-equation-to-dictionary) and do the same things as numpy_from_dicts(_dictionaries_)

```py
system_roots = g_equations.np_handler.numpy_from_equs([
    "3x - y + 2z = -4",
    "x + 4y - z = 10",
    "2x + 3y + z = 8"
])
```

Both `system_roots` look like:

```
{'x': 0.16666666666666607, 'y': 2.166666666666668, 'z': -1.166666666666666}
```

> [!NOTE]
> There are shorter names for these two functions. `roots_of_dicts` for numpy_from_dicts and `solve_equs` for numpy_from_equs
