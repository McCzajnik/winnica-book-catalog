from django.test import TestCase
from catalog.forms import CreateAuthorForm

"""
General scheme for tests
class YourTestClass(TestCase):

    @classmethod

    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):w
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
"""
#setUpTestData() is called once at the beginning of the test run for class-level setup.
#You'd use this to create objects that aren't going to be modified or changed in any of the test methods.

#setUp() is called before every test function to set up any objects that may be
# modified by the test (every test function will get a "fresh" version of these objects).

#Django specific asserions: https://docs.djangoproject.com/en/1.10/topics/testing/tools/#assertions
# Python assertions: https://docs.python.org/3/library/unittest.html#assert-methods
