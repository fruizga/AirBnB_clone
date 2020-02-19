#!/usr/bin/python3
"""Test Review"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testreview(unittest.TestCase):
    def test_pep8_conformance_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """class"""
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        """class"""
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))

    def test_review(self):
        """
        Test review
        """
        my_place = Place()
        my_user = User()
        my_review = Review()
        my_review.place_id = my_place.id
        my_review.user_id = my_user.id
        my_review.text = 'holberton'
        self.assertEqual(my_review.place_id, my_place.id)
        self.assertEqual(my_review.user_id, my_user.id)
        self.assertEqual(my_review.text, 'holberton')

    def test_value(self):
        """ test value """
        rev = Review()
        self.assertEqual(rev.place_id, "")
        self.assertEqual(rev.user_id, "")
        self.assertEqual(rev.text, "")
        self.assertFalse(rev.text, "was perfect")

    def test_review_type(self):
        """ test review value type """
        rev = Review()
        self.assertEqual(type(rev.place_id), str)
        self.assertEqual(type(rev.user_id), str)
        self.assertNotEqual(type(rev.text), int)

    def test_attribute(self):
        """ review """
        rev = Review()
        self.assertTrue(hasattr(rev, "place_id"))
        self.assertTrue(hasattr(rev, "user_id"))
        self.assertTrue(hasattr(rev, "text"))
        self.assertFalse(hasattr(rev, "area"))

if __name__ == '__main__':
    unittest.main()
