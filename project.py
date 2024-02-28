import argparse
from functools import reduce
from math import sqrt as squareRoot
import sys
from timeit import default_timer as timer


def main() -> None:

    parser = argparse.ArgumentParser(
        description="An application to fine prime numbers and factors",
        add_help=True
    )
    parser.add_argument(
        '-v',
        help="Switches on verbose mode. This will output factors and any prime numbers found",
        action="store_true"
    )
    args = parser.parse_args()
    verbose = getattr(args, 'v')

    print("Please select an option: ")
    print("1. Check if a number is prime")
    print("2. Find all primes up to a number")
    print("3. Find x primes")
    print("4. Exit")

    while True:
        option = input("Enter option: ")
        if option not in ["1", "2", "3", "4"]:
            pass
        elif option == "4":
            sys.exit("Thank you. Exiting now.")
        else:
            break

    while True:
        try:
            number = get_number()
            break
        except ValueError:
            print("Please enter a valid number")
            pass

    if option == "1":
        if is_prime(number):
            print(f"Your number, {number}, is a prime.")
        else:
            print(f"Your number, {number}, is not a prime.")
            if verbose:
                factors = find_factors(number)
                print(f"It has {len(factors):,} factors.")
                print(", ".join(map(str, factors)))
        sys.exit("Thank you, goodbye.")

    if option == "2":
        print("---- Starting ----")
        start = timer()
        primes = find_primes(number)
        end = timer()
        print(f"---- Finished in {end-start:.3f} seconds ----")
        print(f"Here you go. I found {len(primes):,} prime numbers between 2 and {number}.")
        if verbose:
            print(', '.join(map(str, primes)))
        sys.exit("Thank you, goodbye.")

    if option == "3":
        print("---- Starting ----")
        start = timer()
        primes = find_x_primes(number)
        end = timer()
        print(f"---- Finished in {end-start:.3f} seconds ----")
        if verbose:
            print(f"Here you go. I found the first {number:,} primes for you")
            print(", ".join(map(str, primes)))
        sys.exit("Thank you, goodbye.")


def get_number() -> int:
    '''
    Gets a number from the user. Calls valid_input() to check that
    the user input is a valid integer.
    '''

    while True:
        number = input("Please enter a positive integer greater than 1: ")
        if valid_input(number):
            return int(number)
        else:
            print("Please enter a valid number.")


def valid_input(userInput: str) -> bool:
    '''
    Takes in the user input from get_number() and returns True or False
    depending on whether the user inputs a positive integer (2 or greater) or
    not.

    Args:
        userInput (str): The user input to check

    Returns:
        bool: Whether the userInput is a valid integer.

    '''
    try:
        n = int(userInput)
        if n < 2:
            return False
    except ValueError:
        return False
    return True


def is_prime(n: int) -> bool:
    '''
    Takes in an integer and returns True or False depending on whether the
    integer is prime or not.

    Args:
        n (int): The number to check


    Returns:
        bool: Whether n is a prime number or not
    '''
    max = int(squareRoot(n)) + 1
    for i in range(2, max):
        if n % i == 0:
            return False
    return True


def find_primes(n: int) -> list[int]:
    '''
    Takes in an integer, n, and finds all the prime numbers
    between 2 and n.

    Args:
        n (int): The upper bound of the values to check

    Returns:
        list[int]: A list of prime numbers
    '''
    primes = [i for i in range(2, n+1) if is_prime(i)]
    return primes


def find_x_primes(n: int) -> list[int]:
    '''
    Takes in an integer, n, and finds the first n prime numbers.

    Args:
        n (int): The number of prime numbers to find.

    Returns:
        list[int]: A list of n prime numbers
    '''
    primes = []
    current = 2
    while len(primes) < n:
        if is_prime(current):
            primes.append(current)
        current += 1
    return primes


def find_factors(n: int) -> list[int]:
    '''
    Takes in an integer, n, and finds its factors.

    Args:
        n (int): The number to factorise

    Returns:
        list[int]: A list of factors
    '''
    factors = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(squareRoot(n)) + 1) if n % i == 0)))
    return sorted(factors)


if __name__ == "__main__":
    main()
