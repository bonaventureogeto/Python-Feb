import unittest
import csv
from inventory import Item, InventoryManagementSystem

class TestInventoryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.item1 = Item("Item 1", 10, 5.99)
        self.item2 = Item("Item 2", 20, 3.99)
        self.ims = InventoryManagementSystem()

    def test_add_item(self):
        self.ims.add_item(self.item1)
        self.assertEqual(len(self.ims.inventory), 1)
        self.assertEqual(self.ims.inventory[0].name, "Item 1")
        self.assertEqual(self.ims.inventory[0].quantity, 10)
        self.assertEqual(self.ims.inventory[0].price, 5.99)

    def test_remove_item(self):
        self.ims.add_item(self.item1)
        self.ims.add_item(self.item2)
        self.ims.remove_item(self.item1)
        self.assertEqual(len(self.ims.inventory), 1)
        self.assertEqual(self.ims.inventory[0].name, "Item 2")

    def test_update_item_quantity(self):
        self.ims.add_item(self.item1)
        self.ims.update_item(self.item1, quantity=15)
        self.assertEqual(self.ims.inventory[0].quantity, 15)

    def test_update_item_price(self):
        self.ims.add_item(self.item1)
        self.ims.update_item(self.item1, price=6.99)
        self.assertEqual(self.ims.inventory[0].price, 6.99)

    def test_display_inventory(self):
        self.ims.add_item(self.item1)
        self.ims.add_item(self.item2)
        expected_output = "Item 1, 10, 5.99\nItem 2, 20, 3.99\n"
        self.assertEqual(self.ims.display_inventory(), expected_output)

    def test_save_load_inventory(self):
        self.ims.add_item(self.item1)
        self.ims.add_item(self.item2)
        self.ims.save_inventory_to_csv("test_inventory.csv")
        self.ims.load_inventory_from_csv("test_inventory.csv")
        self.assertEqual(len(self.ims.inventory), 2)
        self.assertEqual(self.ims.inventory[0].name, "Item 1")
        self.assertEqual(self.ims.inventory[0].quantity, 10)
        self.assertEqual(self.ims.inventory[0].price, 5.99)
        self.assertEqual(self.ims.inventory[1].name, "Item 2")
        self.assertEqual(self.ims.inventory[1].quantity, 20)
        self.assertEqual(self.ims.inventory[1].price, 3.99)

if __name__ == '__main__':
    unittest.main()
