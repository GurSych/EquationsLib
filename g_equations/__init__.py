def equ_to_dict(equation_str: str) -> dict:
    equation_str = equation_str.replace(' ','')
    equ_pair     = equation_str.split('=')
    if len(equ_pair) != 2:
        raise Exception("g_equations: Equation must have single-one '=' symbol")
    equation_dict        = dict()
    equation_dict["res"] = 0.
    equation_str         = equ_pair[0] + '='

    def go_coefficients(k: float) -> None:
        var_indx = 0
        for i in range(0,len(equation_str)):
            char = equation_str[i]
            if char != '+' and char != '-' and char != '=': continue
            if i == var_indx: continue
            var_str     = equation_str[var_indx:i]
            var_str_len = i - var_indx
            if var_str_len == 0:
                raise Exception("g_equations: Loosing statement between math symbols")
            var_name = var_str[-1]
            if var_name.isalpha():
                var_value     = var_str[:-1]
                var_value_len = var_str_len - 1
                local_k       = k
            else:
                var_value     = var_str
                var_value_len = var_str_len
                var_name      = "res"
                local_k       = -k
            if var_value_len == 0:
                var_value = 1.0
            elif var_value_len == 1 and var_indx != 0:
                if var_indx == '+': var_value =  1.0
                else:               var_value = -1.0
            else:
                try:
                    var_value = float(var_value)
                except ValueError as e:
                    raise ValueError("g_equations: Variable {} has incorect coefficient - {}".format(var_name,e))
            if var_name in equation_dict:
                equation_dict[var_name] += var_value * local_k
            else:
                equation_dict[var_name] = var_value * local_k
            if char == '=': break 
            var_indx = i
            
    go_coefficients(1.)
    equation_str = equ_pair[1] + '='
    go_coefficients(-1.)
    return equation_dict