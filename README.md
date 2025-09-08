# EquationsLib

EquationsLib is my Python module for working with equations (some things are powered by NumPy)

# Using Library

> The library is in development so this section is updated together with library itself

## Library connection

```py
import g_equations
import g_equations.np_handler
```

**Package Requirements:** The g_equations.np_handler module requires NumPy

## Linear equation to dictionary

g_equations module has equ_to_dict(_equation_) function gets an `str` object with human-like written liner equation and returnes a dictionary with variablies' coefficients

```py
equ_dict = g_equations.equ_to_dict("x + 72.3y - 3z = 8.0")
print(equ_dict) # {'res': 8.0, 'x': 1.0, 'y': 72.3, 'z': -3.0}
```

_Section hasn't been finished yet..._