# Функции арифметических операций

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Основная программа калькулятора

if __name__ == "__main__":
    print("Простой калькулятор")

    try:
        # Ввод чисел и выбор операции
        a = float(input("Первое число: "))
        operation = input("Операция (+, -, *, /): ")
        b = float(input("Второе число: "))

        # Выполнение выбранной операции
        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            raise ValueError("Неизвестная операция")

        # Вывод результата
        print("Результат:", result)

    # Обработка ошибок ввода и выбора операции
    except ValueError as error:
        print("Ошибка:", error)
