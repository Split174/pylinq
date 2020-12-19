import unittest
from collections import namedtuple
from uglyfunc.linq import Linq

People = namedtuple("People", ["firstname", "lastname", "age"])

class TestLinq(unittest.TestCase):
    def setUp(self):
        self.test_people = [People("Sergey", "Popov", "23"),
                            People("Anton", "Vivaldi", "21"),
                            People("Jirok", "Kiv", "45"),
                            People("Sergey", "OrkJump", "17"),
                            People("OddHub", "Doter", "33")]

    def test_select_gt_age25_two_people(self):
        people = Linq(self.test_people).select(lambda x: x.age > 25)
        self.assertEqual(len(people), 2)

    def test_select_name_sergey_two_people(self):
        people = Linq(self.test_people).select(lambda x: x.firstname == "Sergey")
        self.assertEqual(len(people), 2)