equation = input('Введите /,*,+ или -, через пробелы введите первое и второе числа, например + 2 2 : ')
formula = equation.split()
assert (formula[0] == '/' or formula[0] == '*' or formula[0] == '-' or formula[0] == '+'), 'Нет такой операции'
def solve(expression):
    if expression[0] == '+':
        print(int(expression[1]) + int(expression[2]))
    if expression[0] == '-':
        print(int(expression[1]) - int(expression[2]))
    if expression[0] == '*':
        print(int(expression[1]) * int(expression[2]))
    if expression[0] == '/':
        print(int(expression[1]) / int(expression[2]))
try:
    solve(formula)
except ZeroDivisionError:
    print(f"Делить на ноль нельзя")
except ValueError :
    print("У нас не целые числа на входе")
except Exception:
 	print(Exception)
