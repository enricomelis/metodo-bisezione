# The script still needs to be finished

import sympy as sp

def calc_func(func_input, x, x0):
    try:
        func = sp.simplify(func_input)
        f = sp.lambdify(x, func, 'math')
        result = f(x0)
        print(f'f(x) = {func} at x = {x0} is {result}')
        return result

    except Exception:
        print(f"Error: {Exception}")

def calc_sign(f_x):
    if f_x < 0:
        return 'negative'
    else:
        return 'positive'

def check_existence(f_a, f_b):
    if(f_a * f_b < 0):
        existence = True
    else:
        existence = False
    
    return existence

def bisection_method():
    print("")

def main():
    function_input = input("Enter a f(x): ")
    x = sp.Symbol('x')

    # Input Control
    request_loop = True
    while(request_loop):
        a = float(input("Enter bottom value 'a': "))
        b = float(input("Enter bottom value 'b': "))

        if(a < b):
            request_loop = False
        

    f_a = calc_func(function_input, x, a)
    f_a_sign = calc_sign(f_a)
    f_b = calc_func(function_input, x, b)
    f_b_sign = calc_sign(f_b)

    zero_exists = check_existence(f_a, f_b)

    if(not(zero_exists)):
        print("There is not solution in the given range, try with another function or another range.")
    else:
        M = float((a+b)/2)
        f_M = calc_func(function_input, x, M)

        if(f_M == 0):
            print(f"Solution found: f(x) at x = {M} is a solution.")
            return

        f_M_sign = calc_sign(f_M)

        if f_M_sign != f_a_sign:
            zero_exists = check_existence(f_a, f_M)
            print(zero_exists)
        else:
            zero_exists = check_existence(f_b, f_M)
            print(zero_exists)


main()