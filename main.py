
total_seats = 50
available_seats = list(range(1, total_seats + 1))
bookings = {}  
booking_id_counter = 1


def check_availability():
    print(f"\nAvailable Seats: {len(available_seats)}")
    print("Seat Numbers:", available_seats)


def book_ticket():
    global booking_id_counter

    if not available_seats:
        print("\nNo seats available!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    seat = available_seats.pop(0)  
    booking_id = booking_id_counter

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat
    }

    booking_id_counter += 1

    print("\nTicket Booked Successfully!")
    print(f"Booking ID: {booking_id}")
    print(f"Seat Number: {seat}")


def view_ticket():
    booking_id = int(input("Enter Booking ID: "))

    if booking_id in bookings:
        details = bookings[booking_id]
        print("\n--- Ticket Details ---")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Seat Number: {details['seat']}")
    else:
        print("\nInvalid Booking ID!")


def cancel_ticket():
    booking_id = int(input("Enter Booking ID to Cancel: "))

    if booking_id in bookings:
        seat = bookings[booking_id]["seat"]
        available_seats.append(seat)
        available_seats.sort()

        del bookings[booking_id]

        print("\nTicket Cancelled Successfully!")
    else:
        print("\nInvalid Booking ID!")


while True:
    print("\n===== Railway Reservation System =====")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_availability()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Please try again.")
