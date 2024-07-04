# Seat Booking Application

# Create a map for the users with the letters to see if the seat is
seat_map = [['F' for _ in range(80)] for _ in range(6)]  # 6 rows, 80 columns

# Define a function to check availability of a seat
def check_availability():
# Inputs for the user to check the availability of the seat
    row = int(input("Enter row number (1-6): "))
    col = int(input("Enter column number (1-80): "))
# Check if the seat is available by checking the map
    if seat_map[row-1][col-1] == 'F':
# If the seat is equal to 'F', then print that it is available
        print("Seat is available.")
# If it is not available it needs to be notified to the user
    else:
        print("Seat is not available.")

# Book a seat feature
def book_seat():
# Inputs to get the user's seat selection
    row = int(input("Enter row number (1-6): "))
    col = int(input("Enter column number (1-80): "))
# Check in the seat map if the introduced seat is avalilable
    if seat_map[row-1][col-1] == "F":
# If it is free the value will pass from F to R
        seat_map[row-1][col-1] = "R"
# Print that it has been booked successfully
        print("Seat has been booked successfully")
# If it is not available, notify the user
    else:
        print("Seat is occupied")

# Define a function to free a seat
def free_seat():
# Inputs for the user to select the seat
    row = int(input("Enter row number (1-6): "))
    col = int(input("Enter column number (1-80): "))
# Change the values of the seat from R to F to free it.
    if seat_map[row-1][col-1] == 'R':
        seat_map[row-1][col-1] = 'F'
        print("Seat freed successfully.")
# If the seat is not booked, then notify the user that the seat is already free
    else:
        print("Seat is already free.")

# Create a function to show the booking state
def booking_state():
    for row in seat_map:
        print(' '.join(row))

# Main interface loop to keep the program open

while True:
#Print the options of the menu that the user can access
    print("\nSeat Booking Application Menu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")
#Input to get the choice that the user wants
    choice = int(input("Enter your choice: "))
# Give access depending on the number selected to the diferent functions in the app
    if choice == 1:
        check_availability()
    elif choice == 2:
        book_seat()
    elif choice == 3:
        free_seat()
    elif choice == 4:
        booking_state()
# If the user ask for closing the app break or close the program
    elif choice == 5:
        print("Exiting program. Goodbye!")
        break
# If the user gives another number it should put a message that the number is invalid and to try again
    else:
        print("Invalid choice. Please try again.")


