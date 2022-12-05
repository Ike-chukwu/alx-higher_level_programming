#!/usr/bin/python3
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """ Unit tests for testing instantiation of the Base class """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_automatically(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertTrue(b1, self.id == 1)
        self.assertTrue(b2, self.id == 2)
        self.assertTrue(b3, self.id == 3)
        self.assertTrue(b4, self.id == 12)
        self.assertTrue(b5, self.id == 4)

    def test_1_id(self):
        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 2)

    def test_to_json_string(self):
        dic1 = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        dic2 = {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10}
        string = Base.to_json_string([dic1, dic2])
        self.assertTrue(type(dic1) == dict)
        self.assertTrue(type(dic2) == dict)
        self.assertTrue(type(string) == str)
        self.assertTrue(string,
                [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
                    {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10}])

    def test_empty_to_json_string(self):
        dic3 = {}
        stri = Base.to_json_string([dic3])
        self.assertTrue(type(stri) == str)
        self.assertTrue(len(dic3) == 0)
        self.assertTrue(stri, [])

    def test_none_to_json_string(self):
        dic4 = None
        stri = Base.to_json_string([dic4])
        self.assertTrue(type(stri) == str)
        self.assertTrue(stri, [])


