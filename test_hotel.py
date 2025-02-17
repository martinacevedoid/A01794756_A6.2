import unittest
import os
from reservation_system import Hotel, HOTEL_FILE, load_data, save_data

class TestHotel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up initial test data before tests run"""
        if not os.path.exists("data"):
            os.makedirs("data")
        save_data(HOTEL_FILE, {})

    def setUp(self):
        """Run before every test"""
        save_data(HOTEL_FILE, {})

    def test_create_hotel(self):
        """Test creating a hotel"""
        Hotel.create_hotel("H1", "Luxury Inn", "New York", 5)
        hotels = load_data(HOTEL_FILE)
        self.assertIn("H1", hotels)

    def test_delete_hotel(self):
        """Test deleting a hotel"""
        Hotel.create_hotel("H1", "Luxury Inn", "New York", 5)
        Hotel.delete_hotel("H1")
        hotels = load_data(HOTEL_FILE)
        self.assertNotIn("H1", hotels)

    def test_modify_hotel(self):
        """Test modifying hotel information"""
        Hotel.create_hotel("H1", "Luxury Inn", "New York", 5)
        Hotel.modify_hotel("H1", name="Grand Palace", location="Los Angeles")
        hotels = load_data(HOTEL_FILE)
        self.assertEqual(hotels["H1"]["name"], "Grand Palace")

    def test_reserve_room(self):
        """Test reserving a room"""
        Hotel.create_hotel("H1", "Luxury Inn", "New York", 5)
        Hotel.reserve_room("H1")
        hotels = load_data(HOTEL_FILE)
        self.assertEqual(hotels["H1"]["rooms_available"], 4)

    def test_cancel_reservation(self):
        """Test canceling a reservation"""
        Hotel.create_hotel("H1", "Luxury Inn", "New York", 5)
        Hotel.reserve_room("H1")
        Hotel.cancel_reservation("H1")
        hotels = load_data(HOTEL_FILE)
        self.assertEqual(hotels["H1"]["rooms_available"], 5)

if __name__ == "__main__":
    unittest.main()
