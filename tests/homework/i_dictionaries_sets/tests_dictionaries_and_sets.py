#

import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory,remove_inventory_widget,inventory

class Test_Config (unittest.TestCase):

    def test_add_inventory (self):
        add_inventory ("Widget1",10)
        self.assertEqual (inventory ["Widget1"],10)

        add_inventory ("Widget1",25)
        self.assertEqual (inventory ["Widget1"],35)

        add_inventory ("Widget1", -10)
        self.assertEqual (inventory ["Widget1"],25)


    def test_remove_inventory_widget (self):

        add_inventory ("Widget1", 10)
        add_inventory ("Widget2", 20)

        removed= remove_inventory_widget ("Widget1")
        self.assertTrue (removed)
        self.assertEqual (len (inventory),1)
        self.assertIn ("Widget2", inventory)

        