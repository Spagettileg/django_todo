from django.test import TestCase
from .forms import ItemForm
"""
All tests performed map over to functions in forms.py file
"""

# Create your tests here.
class TestToDoItemForm(TestCase):
    
    def test_can_create_an_item_with_just_a_name(self):  # Method defined 
        form = ItemForm({'name': 'Create Tests'})  # Create a dictionary in {}
        self.assertTrue(form.is_valid())  # Test the is_valid function
        
    def test_correct_message_for_missing_name(self):  # Method defined
        form = ItemForm({'name': ''})  # Key is present & Value is missing
        self.assertFalse(form.is_valid())  # Test the is_valid function
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        """
        We want to assert there is an error in the name & we want to assert
        an error in the value where no data can be read. A warning message
        'This field is required' will then appear.
        """
        