def equ_to_dict(equation_str: str) -> dict:
    equation_dict        = dict()
    equation_str         = equation_str.replace(' ','')
    equ_pair             = equation_str.split('=')
    equation_dict["res"] = float(equ_pair[1])
    equation_str         = equ_pair[0]
    var_indx             = [-1]
    for i in range(0,len(equation_str),1):
        if equation_str[i].isalpha():
            var_indx.append(i)
    for i in range(1,len(var_indx),1):
        var_str   = equation_str[(var_indx[i-1]+1):(var_indx[i]+1)]
        var_name  = var_str[-1]
        if var_str[0] == '+':
            var_sign  = 1.
            var_value = var_str[1:-1]
        elif var_str[0] == '-':
            var_sign  = -1.
            var_value = var_str[1:-1]
        elif i == 1:
            var_sign  = 1.
            var_value = var_str[:-1]
        else:
            raise ValueError("g_equations: Variable {} must have a sign!".format(var_name))
        if len(var_value) == 0: 
            var_value = 1.0
        else:
            try:
                var_value = float(var_value)
            except ValueError:
                raise ValueError("g_equations: Variable {} has incorect coefficient!".format(var_name))
        if var_name in equation_dict:
            equation_dict[var_name] += var_value * var_sign
        else:
            equation_dict[var_name] = var_value * var_sign
    return equation_dict