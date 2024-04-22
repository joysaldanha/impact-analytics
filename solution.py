"""
## Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. You are not
allowed to miss classes for four or more consecutive days. Your graduation ceremony is on the last day of the academic
year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the
fraction to decimal

Test cases:

for 5 days: 14 / 29
for 10 days: 372 / 773
"""

# Problem Solution
# Run solution.py file and give input to check test cases


# 1. finds total number of ways to attend class over N days
# 2. finds probability of missing graduation day
def calculate_ways_to_attend_class(days: int):
    # invalid inputs
    if days <= 0:
        raise ValueError(f"Invalid input {days}. Input should be positive")

    # ways to attend class over the first 3 days
    dp_ways = [2 ** i for i in range(4)]

    # if days is less than 4, then missing 4 days is not possible
    # return all possibilities
    if days < 4:
        return dp_ways[days], dp_ways[days-1]

    # loop from day 4 to day N
    for _ in range(4, days + 1):
        nth_day_present = dp_ways[-1]
        nth_day_absent = sum(dp_ways[:-1])
        dp_ways = dp_ways[1:] + [nth_day_absent + nth_day_present]

    # return solution for N days
    ways_to_attend_class = dp_ways[-1]
    probability_to_miss_graduation = dp_ways[-1] - dp_ways[-2]
    return ways_to_attend_class, probability_to_miss_graduation


def main():
    # take input and store
    try:
        no_of_days = int(input("Enter the value of N\n"))
    except ValueError:
        print(f"Input value not integer")
        return

    # calculate solution
    try:
        ways_to_attend_class, probability_to_miss_graduation = calculate_ways_to_attend_class(no_of_days)
        print(f"Number of ways to attend class of {no_of_days} days: {ways_to_attend_class}")
        print(f"Probability to miss graduation: {probability_to_miss_graduation}/{ways_to_attend_class}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
