import project
import pytest


def test_is_prime_prime():
    assert project.is_prime(3) == True


def test_is_prime_nonprime():
    assert project.is_prime(6) == False


def test_find_primes_single():
    assert project.find_primes(2) == [2]


def test_find_primes_multiple():
    assert project.find_primes(10) == [2, 3, 5, 7]


def test_find_x_primes_single():
    assert project.find_x_primes(1) == [2]


def test_find_x_primes_multiple():
    assert project.find_x_primes(5) == [2, 3, 5, 7, 11]


def test_find_factors_odd():
    assert project.find_factors(9) == [1, 3, 9]


def test_find_factors_even():
    assert project.find_factors(20) == [1, 2, 4, 5, 10, 20]


def test_find__factors_prime():
    assert project.find_factors(11) == [1, 11]


def test_valid_input_word():
    assert project.valid_input("Cat") == False


def test_valid_input_blank():
    assert project.valid_input("") == False


def test_valid_input_number():
    assert project.valid_input("10") == True
