import unittest
from dataclasses import dataclass
from uglyfunc.linq import Linq

@dataclass
class People:
    firstname: str
    lastname: str
    age: int

class TestLinq(unittest.TestCase):
    def setUp(self):
        self.test_people = [People("Sergey", "Popov", 23),
                            People("Anton", "Vivaldi", 21),
                            People("Jirok", "Kiv", 45),
                            People("Sergey", "OrkJump", 17),
                            People("OddHub", "Doter", 33)]

    def test_where_gt_age25_two_people(self):
        people = Linq(self.test_people).where(lambda x: x.age > 25)
        self.assertEqual(len(people), 2)

    def test_where_name_sergey_two_people(self):
        people = Linq(self.test_people).where(lambda x: x.firstname == "Sergey")
        self.assertEqual(len(people), 2)

    def test_order_by_age(self):
        expect = list(sorted(self.test_people, key=lambda x: x.age))
        real = Linq(self.test_people).order_by(lambda x: x.age).to_list()
        self.assertEqual(real, expect)

    def test_order_by_desc_age(self):
        expect = list(sorted(self.test_people, key=lambda x: x.age, reverse=True))
        real = Linq(self.test_people).order_by_descending(lambda x: x.age).to_list()
        self.assertEqual(real, expect)

    def test_select_age(self):
        age_list = Linq(self.test_people).select(lambda x: x.age).to_list()
        self.assertEqual(age_list, [23, 21, 45, 17, 33])

    def test_any_firstname_seva_false(self):
        real = Linq(self.test_people).any(lambda x: x.firstname == "Seva")
        self.assertEqual(real, False)

    def test_any_firstname_jirok_true(self):
        real = Linq(self.test_people).any(lambda x: x.firstname == "Jirok")
        self.assertEqual(real, True)

    def test_reverse_and_select_age(self):
        age_list = Linq(self.test_people).select(lambda x: x.age).reverse().to_list()
        self.assertEqual(age_list, [33, 17, 45, 21, 23])

    def test_all_age_gt_15_true(self):
        real = Linq(self.test_people).all(lambda x: x.age > 15)
        self.assertEqual(real, True)

    def test_all_name_equal_sergey_false(self):
        real = Linq(self.test_people).all(lambda x: x.firstname == "Sergey")
        self.assertEqual(real, False)

    def test_count_without_cond_5(self):
        real = Linq(self.test_people).count()
        self.assertEqual(real, 5)

    def test_count_age_gt_25_2(self):
        real = Linq(self.test_people).count(lambda x: x.age > 25)
        self.assertEqual(real, 2)