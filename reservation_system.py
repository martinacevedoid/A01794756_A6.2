"""
Reservation System Module

This module manages hotels, customers, and reservations.
Enables CRUD operations and JSON-based data persistence for entities.
"""

import json
import os

# File paths for persistence
DATA_PATH = "data"
HOTEL_FILE = os.path.join(DATA_PATH, "hotels.json")
CUSTOMER_FILE = os.path.join(DATA_PATH, "customers.json")
RESERVATION_FILE = os.path.join(DATA_PATH, "reservations.json")

# Ensure data directory exists
if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)


def load_data(file_path):
    """Load data from a JSON file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {file_path}")
            return {}
    return {}


def save_data(file_path, data):
    """Save data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


class Hotel:
    """Represents a hotel with available rooms."""

    def __init__(self, hotel_id, name, location, rooms_available):
        """Initialize a new Hotel object."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self):
        """Convert Hotel object to dictionary."""
        return self.__dict__

    @staticmethod
    def create_hotel(hotel_id, name, location, rooms_available):
        """Create a new hotel and store it in the database."""
        hotels = load_data(HOTEL_FILE)
        if hotel_id in hotels:
            print("Error: Hotel ID already exists.")
            return
        hotels[hotel_id] = Hotel(
            hotel_id, name, location, rooms_available
        ).to_dict()
        save_data(HOTEL_FILE, hotels)

    @staticmethod
    def delete_hotel(hotel_id):
        """Delete a hotel from the database."""
        hotels = load_data(HOTEL_FILE)
        if hotel_id in hotels:
            del hotels[hotel_id]
            save_data(HOTEL_FILE, hotels)
        else:
            print("Error: Hotel not found.")

    @staticmethod
    def display_hotels():
        """Retrieve and return all hotels."""
        return load_data(HOTEL_FILE)

    @staticmethod
    def modify_hotel(hotel_id, name=None, location=None, rooms_available=None):
        """Modify an existing hotel's details."""
        hotels = load_data(HOTEL_FILE)
        if hotel_id in hotels:
            if name:
                hotels[hotel_id]["name"] = name
            if location:
                hotels[hotel_id]["location"] = location
            if rooms_available is not None:
                hotels[hotel_id]["rooms_available"] = rooms_available
            save_data(HOTEL_FILE, hotels)
        else:
            print("Error: Hotel not found.")

    @staticmethod
    def reserve_room(hotel_id):
        """Reserve a room in a specified hotel."""
        hotels = load_data(HOTEL_FILE)
        if hotel_id in hotels and hotels[hotel_id]["rooms_available"] > 0:
            hotels[hotel_id]["rooms_available"] -= 1
            save_data(HOTEL_FILE, hotels)
        else:
            print("Error: No rooms available or hotel not found.")

    @staticmethod
    def cancel_reservation(hotel_id):
        """Cancel a room reservation and increase availability."""
        hotels = load_data(HOTEL_FILE)
        if hotel_id in hotels:
            hotels[hotel_id]["rooms_available"] += 1
            save_data(HOTEL_FILE, hotels)
        else:
            print("Error: Hotel not found.")


class Customer:
    """Represents a customer with personal details."""

    def __init__(self, customer_id, name, email):
        """Initialize a new Customer object."""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert Customer object to dictionary."""
        return self.__dict__

    @staticmethod
    def create_customer(customer_id, name, email):
        """Create a new customer and store it in the database."""
        customers = load_data(CUSTOMER_FILE)
        if customer_id in customers:
            print("Error: Customer ID already exists.")
            return
        customers[customer_id] = Customer(
            customer_id, name, email
        ).to_dict()
        save_data(CUSTOMER_FILE, customers)

    @staticmethod
    def delete_customer(customer_id):
        """Delete a customer from the database."""
        customers = load_data(CUSTOMER_FILE)
        if customer_id in customers:
            del customers[customer_id]
            save_data(CUSTOMER_FILE, customers)
        else:
            print("Error: Customer not found.")

    @staticmethod
    def display_customers():
        """Retrieve and return all customers."""
        return load_data(CUSTOMER_FILE)

    @staticmethod
    def modify_customer(customer_id, name=None, email=None):
        """Modify an existing customer's details."""
        customers = load_data(CUSTOMER_FILE)
        if customer_id in customers:
            if name:
                customers[customer_id]["name"] = name
            if email:
                customers[customer_id]["email"] = email
            save_data(CUSTOMER_FILE, customers)
        else:
            print("Error: Customer not found.")


class Reservation:
    """Handles reservation functionalities."""

    @staticmethod
    def create_reservation(reservation_id, customer_id, hotel_id):
        """Create a new reservation if the customer and hotel exist."""
        reservations = load_data(RESERVATION_FILE)
        hotels = load_data(HOTEL_FILE)
        customers = load_data(CUSTOMER_FILE)

        if hotel_id not in hotels or customer_id not in customers:
            print("Error: Invalid hotel or customer.")
            return

        if hotels[hotel_id]["rooms_available"] <= 0:
            print("Error: No rooms available.")
            return

        reservations[reservation_id] = {
            "customer_id": customer_id,
            "hotel_id": hotel_id,
        }
        hotels[hotel_id]["rooms_available"] -= 1
        save_data(RESERVATION_FILE, reservations)
        save_data(HOTEL_FILE, hotels)

    @staticmethod
    def cancel_reservation(reservation_id):
        """Cancel a reservation and free up the hotel room."""
        reservations = load_data(RESERVATION_FILE)
        hotels = load_data(HOTEL_FILE)

        if reservation_id in reservations:
            hotel_id = reservations[reservation_id]["hotel_id"]
            hotels[hotel_id]["rooms_available"] += 1
            del reservations[reservation_id]
            save_data(RESERVATION_FILE, reservations)
            save_data(HOTEL_FILE, hotels)
        else:
            print("Error: Reservation not found.")
