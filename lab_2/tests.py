from main import mainFunc
import unittest

class TestMySolution(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(mainFunc(), [9, 3])
if __name__ == '__main__':
    unittest.main()

#1) вложить значения в функцию передавемую в тестах, чтобы не было никакого ввода но он был вынесен в отдельную функцию
# 2) сделать ещё несколько тестов ломающих код
#3) дополнить редми грамотно