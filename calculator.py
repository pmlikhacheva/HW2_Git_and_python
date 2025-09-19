
def main():
    expression = input("Введите выражение: ")
    parts = expression.split()

    if len(parts) != 3:
        print("Invalid input argument")
        return

    num1 = float(parts[0])
    sign = parts[1]
    num2 = float(parts[2])

    if sign == '/':
        result = divide(num1, num2)
    elif sign == '*':
        result = multiply(num1, num2)
#     Коллеги, ниже добавьте свои методы(+,-,*)
    else:
        print("Invalid operator")
        return
    print("Result: " + str(result))

    return result


def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero is not allowed")
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

while True:
    main()
