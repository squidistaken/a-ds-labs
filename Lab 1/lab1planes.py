"""
File: lab1planes.py
Authors: Marcus Persson (m.h.o.persson@student.rug.nl), Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    This program determines which order the planes landing at the airport will be given clearance to leave again
"""

from queue import Queue
from stack import Stack

RUNWAY_LENGTH = 7
HANGAR_SIZE = 5


def get_flights() -> list[tuple]:
    """
    Gets all flights (Aircraft name, checkup) as an input.
    :return: List of tuples (Aircraft name, checkup)
    """

    lst = []

    while True:
        t = input()
        if t == "":
            break
        flight = (t[:-3].strip(), t[-3:].strip())
        lst.append(flight)

    return lst


def main() -> None:
    """
    This function is initialised on runtime.
    """

    # Initialised variables
    flights = get_flights()
    results = []
    runway = Queue()
    hanger = Stack()

    def dequeue_runway() -> None:
        """
        This helper function clears the runway and sends the planes to the results.
        """

        while True:
            if runway.size() == 0:
                break
            results.append(runway.dequeue())

    def pop_hanger() -> None:
        """
        This helper functions clears the hangar and send the planes to results.
        """

        while True:
            if hanger.size() == 0:
                break
            results.append(hanger.pop())

    for flight in flights:
        # There is a need for repairs.
        if flight[1] == "yes":
            hanger.push(flight)
        else:
            runway.enqueue(flight)

        # Reaching waiting runway maximum.
        if runway.size() >= RUNWAY_LENGTH:
            # Unloading runway.
            while runway.size() != 0:
                results.append(runway.dequeue())

        # Reaching hanger maximum.
        if hanger.size() >= HANGAR_SIZE:
            dequeue_runway()
            pop_hanger()

    dequeue_runway()
    pop_hanger()

    print_results(results)


def print_results(flights: list) -> None:
    """
    Prints the results.
    :param flights: List of departure planes.
    """
    for flight in flights:
        print(flight[0])


# Runtime
main()
