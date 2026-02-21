#include <stdio.h>

#define MAX_FLIGHTS 10
#define MAX_NAME_LENGTH 50
#define MAX_PASSENGERS 50

typedef struct {
    int flightNumber;
    char destination[MAX_NAME_LENGTH];
    int availableSeats;
} Flight;

typedef struct {    
    char name[MAX_NAME_LENGTH];
    int seatNumber;
} Passenger;

void displayMenu() {
    printf("\n1. Display Flights\n");
    printf("2. Reserve Seat\n");
    printf("3. Display Passengers\n");
    printf("4. Exit\n");
}

void displayFlights(Flight flights[], int numFlights) {
    printf("\nFlight Number\tDestination\tAvailable Seats\n");
    for (int i = 0; i < numFlights; ++i) {
        printf("%d\t\t%s\t\t%d\n", flights[i].flightNumber, flights[i].destination, flights[i].availableSeats);
    }
}

void reserveSeat(Flight *flight, Passenger passengers[], int *numPassengers) {
    if (flight->availableSeats > 0) {
        printf("\nEnter passenger name: ");
        scanf("%s", passengers[*numPassengers].name);
        passengers[*numPassengers].seatNumber = flight->availableSeats;
        (*numPassengers)++;
        flight->availableSeats--;
        printf("\nReservation successful!\n");
    } else {
        printf("\nSorry, no available seats on this flight.\n");
    }
}

void displayPassengers(Passenger passengers[], int numPassengers) {
    printf("\nPassenger Name \tSeat Number       \t \n");
    for (int i = 0; i < numPassengers; ++i) {
        printf("%s\t\t%d\n", passengers[i].name, passengers[i].seatNumber);
    }
}

int main() {
    Flight flights[MAX_FLIGHTS] = {
        {101, "\t     New York\t",10 },
        {102, "\t     Los Angeles ",15},
        {103, "\t     Chicago \t", 20},
        {104, "\t     Spain  \t",14},
        {105, "\t     Singapore\t",12},
        {106, "\t     Japan   \t",20},
        {107, "\t     Norway  \t",13}
    };

    int numFlights = sizeof(flights) / sizeof(flights[0]);

    Passenger passengers[MAX_PASSENGERS];
    int numPassengers = 0;

    int choice;
    do {
        displayMenu();
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                displayFlights(flights, numFlights);
                break;
            case 2: {
                int flightNumber;
                printf("\nEnter the flight number to reserve a seat: ");
                scanf("%d", &flightNumber);

                int index = -1;
                for (int i = 0; i < numFlights; ++i) {
                    if (flights[i].flightNumber == flightNumber) {
                        index = i;
                        break;
                    }
                }

                if (index != -1) {
                    reserveSeat(&flights[index], passengers, &numPassengers);
                } else {
                    printf("\nInvalid flight number.\n");
                }
                break;
            }
            case 3:
                displayPassengers(passengers, numPassengers);
                break;
            case 4:
                printf("\nExiting the program. Thank you!\n");
                break;
            default:
                printf("\nInvalid choice. Please try again.\n");
        }
    } while (choice != 4);

    return 0;
}
