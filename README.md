# Robot Distance Sensor Program

## 1. What does this program do?
This program acts as the "brain" of a robot that has a distance sensor.
The sensor gives the robot a list of distances (in meters) to nearby
obstacles. For each distance in the list, the program decides what the
robot should do next:

- **Distance less than 0.5m** → `STOP` (obstacle too close)
- **Distance between 0.5m and 1m** → `SLOW` (obstacle nearby)
- **Distance more than 1m** → `MOVE FAST` (path is clear)

**Example:**
```
Input:  [0.3, 1.5, 0.8, 2.0, 0.4]
Output: ['STOP', 'MOVE FAST', 'SLOW', 'MOVE FAST', 'STOP']
```

## 2. How does the Robot class work?
The `Robot` class represents one robot. When you create a robot, you
give it:
- `name` — the robot's name (e.g., `"Wall-E"`)
- `battery` — its starting battery percentage (defaults to `100` if not given)

Example:
```python
my_robot = Robot("Wall-E", battery=85)
```

The class stores this information so it can be used later, for example
to check the robot's battery status.

## 3. What does each method do?

### `check_distances(distances)`
This is the main method. It takes a **list** of distance readings and
returns a **list** of decisions (`STOP`, `SLOW`, or `MOVE FAST`), one
for each distance, using the rules above.

It also protects against bad data:
- If `distances` isn't a list → raises a `TypeError`
- If the list is empty → raises a `ValueError`
- If any item isn't a number → raises a `TypeError`
- If any item is negative (distances can't be negative) → raises a `ValueError`

### `battery_status()`
A helper method that looks at `self.battery` and returns a simple
description:
- `20% or less` → `"Low"`
- `21% - 70%` → `"Medium"`
- `71% - 100%` → `"Full"`

## 4. How do I run the code?
1. Make sure you have Python 3 installed.
2. Download `robot.py` from this repository.
3. Open a terminal in the folder where the file is saved.
4. Run:
   ```
   python robot.py
   ```
5. You'll see the results of all 7 test cases printed to the screen,
   including two error-handling tests that show the program catching
   bad input correctly.

## 5. What did I learn from using AI?
Using Claude to help write this code showed how helpful it is to break
a problem into small, clear rules first (STOP / SLOW / MOVE FAST)
before writing any code. It also helped me think about edge cases I
might have missed on my own, like what happens if the distance list is
empty, contains text instead of numbers, or contains a negative
number. Writing the test cases alongside the code — instead of after —
made it much easier to check that each rule actually worked as
expected, including the tricky boundary values exactly at 0.5m and 1m.
