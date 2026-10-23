import unittest
from calculator import add, subtract, multiply, divide


# Тестирование арифметических операций

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


# Запуск тестов

if __name__ == "__main__":
    unittest.main()
