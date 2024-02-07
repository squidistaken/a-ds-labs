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
    Where the magic happens
    :return: list of tuples (aircraft_name,
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

    def deqeueRunway():
        while True:
            if runway.size() == 0:
                break
            results.append(runway.dequeue())

    def popHanger():
        while True:
            if hanger.size() == 0:
                break
            results.append(hanger.pop())

    flights = main()
    results = []

    runway = Queue()
    hanger = Stack()

    for flight in flights:

        if flight[2] == "yes":
            hanger.push(flight)
        else:
            runway.enqueue(flight)

        if runway.size() == RUNWAY_LENGTH:
            #Too lazy to think it though. Might need to add a -1 to runway length
            while True:
                if runway.size() == 0:
                    break
                results.append(runway.dequeue())

        if hanger.size() == HANGAR_SIZE:

            deqeueRunway()
            popHanger()

    deqeueRunway()
    popHanger()


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

main()
