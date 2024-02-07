"""
File:   lab1planes.py
Authors: Marcus Persson () && Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:

"""

from queue import Queue
from stack import Stack

RUNWAY_LENGTH = 7
HANGAR_SIZE = 5


def main():
    """
    just getting the input
    :return: list of tuples (aircraft_name, checkup)
    """

    temp = []

    while True:
        t = input()

        if t == "":
            break

        flight = (t[:-3].strip(), t[-3:].strip())

        temp.append(flight)
    # LET IT BE KNOWN: that I know I can do the whole sorting thing here instead of in a different method.
    return temp


def work():
    """
    This is where the magic happens.
    :return: NA
    """
    def deqeue_runway():
        """
        helper function to clear the runway and send the planes to results
        :return:
        """
        while True:
            if runway.size() == 0:
                break
            results.append(runway.dequeue())

    def pop_hanger():
        """
        helper function to clear the hangar and send planes to results
        :return:
        """
        while True:
            if hanger.size() == 0:
                break
            results.append(hanger.pop())

    flights = main()
    results = []

    runway = Queue()
    hanger = Stack()

    for flight in flights:

        if flight[1] == "yes":
            hanger.push(flight)
        else:
            runway.enqueue(flight)

        if runway.size() == RUNWAY_LENGTH:
            # Too lazy to think it though. Might need to add a -1 to runway length
            while True:
                if runway.size() == 0:
                    break
                results.append(runway.dequeue())

        if hanger.size() == HANGAR_SIZE:
            deqeue_runway()
            pop_hanger()

    deqeue_runway()
    pop_hanger()

    print_results(results)


def print_results(flights: list):
    """
    Simply a print function for the results list
    :param flights: the list of departure planes
    :return: NA
    """
    for flight in flights:
        print(flight[0])


"""
GAME PLAN:

* if for repairs:
* no? -> move to runway
* yes? -> move to hanger

* 7 planes on the waiting runway
* if for full waiting runway: 
* yes? -> all planes depart
* Here a queue data structure needs to be used

* 5 planes in the hanger
* if for full hanger
* yes? -> clear waiting runway && all planes to waiting runway
* Here a stack data structure needs to be used

* end of day (loop)
* 1. clear waiting runway
* 2. move planes from hanger to waiting runway
* 3. clear waiting runway
* --> you can skip the last step and change the second one to simply make all planes depart...
"""

work()
