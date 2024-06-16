import os
from django.test import TestCase

# Set up Environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'project2.settings'

# Create your tests here.
class BasicTest(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
