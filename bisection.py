import sympy as sp

def calc_func(func_input, x, x0):
    try:
        func = sp.simplify(func_input)
        f = sp.lambdify(x, func)
        result = sp.limit(f(x0), x, x0)
        print(f'limit of f(x) = {func} for x tends to {x0} is {result}')
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
        return True
    else:
        print("Because to use this method we need f(a)*f(b)<0, we can't say if there is any solution.")
        return False

def bisection_method(a, b, function_input, x, f_a_sign, f_b_sign):
    M = float((a+b)/2)
    f_M = calc_func(function_input, x, M)

    if(f_M == 0):
        print(f"Solution found: f(x) at x = {M} is a solution.")
        return

    f_M_sign = calc_sign(f_M)

    if f_M_sign != f_a_sign:
        print(f"Solution between {a} and {M}")
        bisection_method(a, M, function_input, x, f_a_sign, f_M_sign)
    else:
        print(f"Solution between {M} and {b}")
        bisection_method(M, b, function_input, x, f_M_sign, f_b_sign)



def main():
    function_input = input("Enter a f(x): ")
    x = sp.Symbol('x')

    # Input Control
    while(True):
        a = float(input("Enter bottom value 'a': "))
        b = float(input("Enter top value 'b': "))

        if(a < b):
            break
        

    f_a = calc_func(function_input, x, a)
    f_a_sign = calc_sign(f_a)
    f_b = calc_func(function_input, x, b)
    f_b_sign = calc_sign(f_b)

    zero_exists = check_existence(f_a, f_b)

    if(not(zero_exists)):
        print("There is not solution in the given range, try with another function or another range.")
    else:
        bisection_method(a, b, function_input, x, f_a_sign, f_b_sign)


main()