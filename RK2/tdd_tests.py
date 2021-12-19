import unittest
import main


class TestStreetsAndHouses(unittest.TestCase):

    def test_task1(self):
        relations = main.relations_creation()
        expected_result = [('Малосемейка', 7000000, 'Пушкинская улица'), ('Сталинка', 20000000, 'Авангардная улица'),
                           ('Хрущевка', 12000000, 'Авангардная улица'), ('Брежневка', 18000000, 'Алтайская улица')]
        self.assertEqual(main.task1(relations[0]), expected_result)
    def test_task2(self):
        relations = main.relations_creation()
        expected_result = [('Авангардная улица', 16000000.0), ('Алтайская улица', 14000000.0), ('Пушкинская улица', 7000000.0)]
        self.assertEqual(main.task2(relations[0]), expected_result)
    def test_task3(self):
        relations = main.relations_creation()
        expected_result = {'Авангардная улица': ['Сталинка', 'Хрущевка'],
                           'Алтайская улица': ['Брежневка', 'Студия'], 'Авиационная улица': ['Малосемейка']}
        self.assertEqual(main.task3(relations[1]), expected_result)

if __name__ == "__main__":
    unittest.main()

