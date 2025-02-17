import unittest
import os
from reservation_system import Hotel, Customer, Reservation, RESERVATION_FILE, load_data, save_data


class TestReservation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up initial test data before tests run"""
        if not os.path.exists("data"):
            os.makedirs("data")
        save_data(RESERVATION_FILE, {})

    def setUp(self):
        """Run before every test"""
        save_data(RESERVATION_FILE, {})

    def test_create_reservation(self):
        """Test creating a reservation"""
        Hotel.create_hotel("H1", "Luxury Inn", "New York", 5)
        Customer.create_customer("C1", "Alice Johnson", "alice@example.com")
        Reservation.create_reservation("R1", "C1", "H1")
        reservations = load_data(RESERVATION_FILE)
        self.assertIn("R1", reservations)

    def test_cancel_reservation(self):
        """Test canceling a reservation"""
        Hotel.create_hotel("H1", "Luxury Inn", "New York", 5)
        Customer.create_customer("C1", "Alice Johnson", "alice@example.com")
        Reservation.create_reservation("R1", "C1", "H1")
        Reservation.cancel_reservation("R1")
        reservations = load_data(RESERVATION_FILE)
        self.assertNotIn("R1", reservations)

if __name__ == "__main__":
    unittest.main()
