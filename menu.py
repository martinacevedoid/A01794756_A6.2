import json
import os
from reservation_system import Hotel, Customer, Reservation  

def main_menu():
    while True:
        print("\nHotel Management System")
        print("1. Hotel Management")
        print("2. Customer Management")
        print("3. Reservation Management")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            hotel_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            reservation_menu()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def hotel_menu():
    while True:
        print("\nHotel Management")
        print("1. Add Hotel")
        print("2. Modify Hotel")
        print("3. Delete Hotel")
        print("4. Display Hotels")
        print("5. Reserve Room")
        print("6. Cancel Reservation")
        print("7. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            hotel_id = input("Enter Hotel ID: ")
            name = input("Enter Hotel Name: ")
            location = input("Enter Location: ")
            rooms = int(input("Enter Number of Rooms: "))
            Hotel.create_hotel(hotel_id, name, location, rooms)
        elif choice == "2":
            hotel_id = input("Enter Hotel ID to Modify: ")
            name = input("Enter New Name (leave blank to keep same): ") or None
            location = input("Enter New Location (leave blank to keep same): ") or None
            rooms = input("Enter New Room Count (leave blank to keep same): ")
            rooms = int(rooms) if rooms else None
            Hotel.modify_hotel(hotel_id, name, location, rooms)
        elif choice == "3":
            hotel_id = input("Enter Hotel ID to Delete: ")
            Hotel.delete_hotel(hotel_id)
        elif choice == "4":
            print("Hotels:", json.dumps(Hotel.display_hotels(), indent=4))
        elif choice == "5":
            hotel_id = input("Enter Hotel ID to Reserve Room: ")
            Hotel.reserve_room(hotel_id)
        elif choice == "6":
            hotel_id = input("Enter Hotel ID to Cancel Reservation: ")
            Hotel.cancel_reservation(hotel_id)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")

def customer_menu():
    while True:
        print("\nCustomer Management")
        print("1. Add Customer")
        print("2. Modify Customer")
        print("3. Delete Customer")
        print("4. Display Customers")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            customer_id = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            email = input("Enter Email: ")
            Customer.create_customer(customer_id, name, email)
        elif choice == "2":
            customer_id = input("Enter Customer ID to Modify: ")
            name = input("Enter New Name (leave blank to keep same): ") or None
            email = input("Enter New Email (leave blank to keep same): ") or None
            Customer.modify_customer(customer_id, name, email)
        elif choice == "3":
            customer_id = input("Enter Customer ID to Delete: ")
            Customer.delete_customer(customer_id)
        elif choice == "4":
            print("Customers:", json.dumps(Customer.display_customers(), indent=4))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

def reservation_menu():
    while True:
        print("\nReservation Management")
        print("1. Create Reservation")
        print("2. Cancel Reservation")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            reservation_id = input("Enter Reservation ID: ")
            customer_id = input("Enter Customer ID: ")
            hotel_id = input("Enter Hotel ID: ")
            Reservation.create_reservation(reservation_id, customer_id, hotel_id)
        elif choice == "2":
            reservation_id = input("Enter Reservation ID to Cancel: ")
            Reservation.cancel_reservation(reservation_id)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
