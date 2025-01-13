import unittest
from age import categorize_by_age


class TestCategorizeByAge(unittest.TestCase):

    def test_child(self):

        ages = range(11)

        for age in ages:
            with self.subTest(number=age):
                self.assertEqual(categorize_by_age(age), 'Child')

    def test_teenager(self):

        ages = range(11,19)

        for age in ages:
            with self.subTest(number=age):
        self.assertEqual(categorize_by_age(age), 'Teenager')

    def test_adult(self):

        ages = range(19 - 60)

        for age in ages:
            with self.subTest(number=age):
        self.assertEqual(categorize_by_age(age), 'Adult')

    def test_senior(self):

        ages = range(60 - 150)

        for age in ages:
            with self.subTest(number=age):
        self.assertEqual(categorize_by_age(age), 'Senior')

    def test_negative_age(self):
        self.assertEqual(categorize_by_age(-5), 'Invalid age: -5.')


    def test_invalid_value(self):

        with self.assertRaises(ValueError):
            categorize_by_age('Hello')


class TestCollection(unittest.TestCase):
    def test_sequence_objects(self):
        a = ('H', 'e', 'l', 'l', 'o')
        b = 'hello'
        self.assertAlmostEqual(a, b)

def test_set_objects(self):
    a = {1, 2, 3}
    b = {3, 2, 1}
    
    self.assertSetEqual(a, b)

if __name__ == '__main__':
    unittest.main()

# Oprócz unittest.skip mamy jeszcze:
# unnittest.skipIf(condition, reason)
# np.condition = sys.version_info < (3, 3)
# unittest.skip