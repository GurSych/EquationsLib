# EquationsLib

EquationsLib is my Python module for working with equations (some things are powered by NumPy)
> _Special thanks to Nastya for her helpful support ^^_

# Using Library

> The library is in development so this section is updated together with library itself

## Library connection

```py
import g_equations
import g_equations.np_handler
```

**Package Requirements:** The g_equations.np_handler module requires NumPy

## Linear equation to dictionary

g_equations module has equ_to_dict(_equation_) function that gets an `str` object with human-like written liner equation and returnes a dictionary with variablies' coefficients

```py
equ_dict = g_equations.equ_to_dict("x + 72.3y - 3z = 8.0")
print(equ_dict) # {'res': 8.0, 'x': 1.0, 'y': 72.3, 'z': -3.0}
```
String should have two parts with `'='` between them: the left part should have only variables and the right one should have only an equavalent value
Returned dictionary will have right side value by `"res"` key and variablies' coefficients by their names

> [!WARNING]
> The function works only with variables whose names consist of a single Latin alphabet character

## Linear equation to matrixs

_Section hasn't been finished yet..._
