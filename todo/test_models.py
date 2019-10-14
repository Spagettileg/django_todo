from django.test import TestCase
from .models import Item
"""
All tests performed map over to functions in models.py file
"""

class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        # If done not properly specified, then False is returned.
        item = Item(name="Create a Test")
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertFalse(item.done)
        
    def test_can_create_an_item_with_a_name_and_status(self):
        # If done not properly specified, then False is returned.
        item = Item(name="Create a Test", done=True)  # Match True assertion
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertTrue(item.done)
        
    def test_item_as_a_string(self):
        # Test name given to object is equal to the item as a string
        item = Item(name="Create a Test")
        self.assertEqual("Create a Test", str(item))
        