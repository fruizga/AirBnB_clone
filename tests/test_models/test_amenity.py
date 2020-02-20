#!/usr/bin/python3
"""Test Amenity"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testamenity(unittest.TestCase):

    def test_pep8_conformance_amenity(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_father(self):
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

    def test_amenity(self):
        """Test attributes of Class Amenity"""
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        self.assertEqual(my_amenity.name, 'Wi-Fi')

    def test_type(self):
        """ test amenity value type """
        amenity1 = Amenity()
        self.assertEqual(type(amenity1.name), str)
        self.assertNotEqual(type(amenity1.name), list)

    def test_attribute(self):
        """ amenity test """
        amenity1 = Amenity()
        self.assertTrue(hasattr(amenity1, "name"))
        self.assertFalse(hasattr(amenity1, "area"))

if __name__ == "__main__":
    unittest.main()
