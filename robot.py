"""
Robot Distance Sensor Program
------------------------------
This program simulates a robot that uses a distance sensor to decide
how it should move. The sensor gives a LIST of distances (in meters),
and for each distance, the robot must decide what to do:

    - distance < 0.5m        -> STOP       (obstacle too close)
    - 0.5m <= distance <= 1m -> SLOW       (obstacle nearby)
    - distance > 1m          -> MOVE FAST  (path is clear)

The Robot class stores the robot's name and battery level, and has a
method that processes a full list of sensor distances and returns the
matching list of decisions. Bad/invalid distance values (negative
numbers, non-numeric values, etc.) are handled with errors instead of
crashing silently.

Example input/output (shown again at the bottom of this file):
    Input:  [0.3, 1.5, 0.8, 2.0, 0.4]
    Output: ['STOP', 'MOVE FAST', 'SLOW', 'MOVE FAST', 'STOP']
"""


class Robot:
    """Represents a robot that has a name, a battery level, and a
    distance sensor used to decide how it should move."""

    def __init__(self, name, battery=100):
        """
        Set up a new robot.

        Parameters:
            name (str): the robot's name.
            battery (int/float): starting battery percentage (default 100).
        """
        self.name = name
        self.battery = battery

    def check_distances(self, distances):
        """
        Look at a list of sensor distances and decide what the robot
        should do for each one.

        Rules:
            distance < 0.5      -> "STOP"
            0.5 <= distance <= 1 -> "SLOW"
            distance > 1         -> "MOVE FAST"

        Parameters:
            distances (list): a list of numbers (int or float), each
                               one a distance reading in meters.

        Returns:
            list: a list of strings ("STOP", "SLOW", or "MOVE FAST"),
                  one for each distance given.

        Raises:
            TypeError: if distances is not a list, or if it contains
                       a value that isn't a number.
            ValueError: if distances is empty, or contains a negative
                        number (a distance can't be negative).
        """
        # --- Error handling for bad input ---
        if not isinstance(distances, list):
            raise TypeError("distances must be a list of numbers.")

        if len(distances) == 0:
            raise ValueError("distances list cannot be empty.")

        decisions = []

        for value in distances:
            # Make sure every item is actually a number
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError(f"Invalid distance value: {value!r} is not a number.")

            # Distances can't be negative in real life
            if value < 0:
                raise ValueError(f"Invalid distance value: {value} cannot be negative.")

            # --- Decision logic ---
            if value < 0.5:
                decisions.append("STOP")
            elif value <= 1:
                decisions.append("SLOW")
            else:
                decisions.append("MOVE FAST")

        return decisions

    def battery_status(self):
        """
        Return a simple description of the robot's current battery level.

        Returns:
            str: "Low", "Medium", or "Full" depending on the battery %.
        """
        if self.battery <= 20:
            return "Low"
        elif self.battery <= 70:
            return "Medium"
        else:
            return "Full"


# ---------------------------------------------------------------------
# TEST CODE (at least 5 test cases)
# ---------------------------------------------------------------------
if __name__ == "__main__":

    my_robot = Robot("Wall-E", battery=85)

    # Test 1: Example from the assignment
    print("Test 1:", my_robot.check_distances([0.3, 1.5, 0.8, 2.0, 0.4]))
    # Expected: ['STOP', 'MOVE FAST', 'SLOW', 'MOVE FAST', 'STOP']

    # Test 2: All distances are far away (path always clear)
    print("Test 2:", my_robot.check_distances([2.5, 3.0, 10.0]))
    # Expected: ['MOVE FAST', 'MOVE FAST', 'MOVE FAST']

    # Test 3: All distances are very close (should always stop)
    print("Test 3:", my_robot.check_distances([0.1, 0.0, 0.49]))
    # Expected: ['STOP', 'STOP', 'STOP']

    # Test 4: Boundary values exactly at 0.5 and 1.0
    print("Test 4:", my_robot.check_distances([0.5, 1.0, 1.01, 0.49]))
    # Expected: ['SLOW', 'SLOW', 'MOVE FAST', 'STOP']

    # Test 5: Error handling - negative distance should raise ValueError
    try:
        my_robot.check_distances([1.0, -0.5, 2.0])
    except ValueError as error:
        print("Test 5:", "Correctly caught error ->", error)

    # Bonus Test 6: Error handling - non-numeric value should raise TypeError
    try:
        my_robot.check_distances([1.0, "close", 2.0])
    except TypeError as error:
        print("Test 6:", "Correctly caught error ->", error)

    # Bonus Test 7: Check battery status method
    print("Test 7:", my_robot.name, "battery status:", my_robot.battery_status())
    # Expected: Wall-E battery status: Medium
