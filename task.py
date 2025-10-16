"""These tasks will help you understand why functions are critical in structuring, simplifying, and reusing code.
Task 1 — Temperature Converter
Goal: Understand why using functions saves effort and errors.

You need to convert a large list of temperature readings between Celsius and Fahrenheit.

Temperatures (in °C): [-10, -5, 0, 12.5, 23.1, 35, 41, 100, 250, 300, 420]

Step 1. (Naive version)
Write plain code (no functions) that converts each Celsius value to Fahrenheit and prints results in a table like:

Celsius | Fahrenheit
------- | -----------
-10     | 14.0
-5      | 23.0
...
Step 2. (Refactored version)
Now create two functions:

def c_to_f(celsius):
    ...

def f_to_c(fahrenheit):
    ...
Use a for loop with your list and print the table again. Finally, show how easily you can reverse the conversion (F→C) for the same list by just changing the function call.

Task 2 — Simple Statistics (Extended)
Goal: Work with multiple cooperating functions and clean structure.

You get a list of numbers entered by the user (space-separated). Create and use four functions:

get_min(numbers)
get_max(numbers)
get_average(numbers)
get_median(numbers)
Each returns its respective value. Handle the case where the user enters no numbers or invalid input (show a friendly error).

Finally, print a short summary like:

Count: 8
Min: 1
Max: 42
Average: 13.5
Median: 10.5
Task 3 — Prime Analyzer
Goal: Create and reuse helper functions to solve a bigger logic problem.

Write:

is_prime(n) — returns True if n is prime.
list_primes(start, end) — returns a list of all primes between start and end.
Ask the user for the range and:

Show the primes,
Count them,
Print the average distance between consecutive primes.
Example:

Range: 10–50
Primes: 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
Count: 11
Average gap: 3.6
Task 4 — Countdown Timer with Text Alerts
Goal: Combine loops, timing, and conditional logic in functions.

Write a function:

import time

def countdown(start, step, alert_every):
    ...
It should:

Print numbers from start down to 0 with pauses of 0.5 seconds (time.sleep(0.5)).
Every alert_every seconds, print a message like "N seconds left!".
If there is no alert_every in the function call, use a default value of 5.
At the end, print "Time’s up!".
Task 5 — Calendar Helper (Advanced)
Goal: Use function composition and data structures.

Write:

is_leap(year) — returns True if leap year.
days_in_month(month, year) — returns number of days in that month (account for leap years).
next_month(month, year) — returns (next_month, next_year) (e.g., 12→1 and increment year).
month_summary(month, year) — prints:

month name,
days count,
leap year info.
Ask the user for a starting month/year, and show info for the next 3 months automatically.

Example:

Enter month: 11
Enter year: 2024

November 2024 – 30 days
December 2024 – 31 days
January 2025 – 31 days (Leap Year: Yes)
✅ Expected skills: conditional logic, tuples, control flow, readable outputs."""
