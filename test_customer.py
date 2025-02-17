import unittest
import os
from reservation_system import Customer, CUSTOMER_FILE, load_data, save_data

class TestCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up initial test data before tests run"""
        if not os.path.exists("data"):
            os.makedirs("data")
        save_data(CUSTOMER_FILE, {})

    def setUp(self):
        """Run before every test"""
        save_data(CUSTOMER_FILE, {})

    def test_create_customer(self):
        """Test creating a customer"""
        Customer.create_customer("C1", "Alice Johnson", "alice@example.com")
        customers = load_data(CUSTOMER_FILE)
        self.assertIn("C1", customers)

    def test_delete_customer(self):
        """Test deleting a customer"""
        Customer.create_customer("C1", "Alice Johnson", "alice@example.com")
        Customer.delete_customer("C1")
        customers = load_data(CUSTOMER_FILE)
        self.assertNotIn("C1", customers)

    def test_modify_customer(self):
        """Test modifying customer information"""
        Customer.create_customer("C1", "Alice Johnson", "alice@example.com")
        Customer.modify_customer("C1", name="Alice Smith", email="alice.smith@example.com")
        customers = load_data(CUSTOMER_FILE)
        self.assertEqual(customers["C1"]["name"], "Alice Smith")

if __name__ == "__main__":
    unittest.main()
