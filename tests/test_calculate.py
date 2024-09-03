import statistics

import pytest
from faker import Faker

from src.main import calculate_route_location

faker = Faker()


def test_calculate_route_location_with_odd_number_of_airports():
    airports = [10, 2, 14, 7, 5]
    assert calculate_route_location(airports) == 7


def test_calculate_route_location_with_even_number_of_airports():
    airports = [10, 2, 14, 7]
    assert calculate_route_location(airports) == (7 + 10) / 2


def test_calculate_route_location_with_empty_list():
    with pytest.raises(ValueError, match="Список аэропортов не может быть пустым."):
        calculate_route_location([])


def test_calculate_route_location_with_large_dataset():
    airports = [faker.random_int(min=0, max=1000) for _ in range(1000)]
    expected_median = statistics.median(airports)
    assert calculate_route_location(airports) == expected_median


def test_calculate_route_location_with_large_even_dataset():
    airports = [faker.random_int(min=0, max=1000) for _ in range(1000)]
    airports.sort()
    expected_median = statistics.median(airports)
    assert calculate_route_location(airports) == expected_median


def test_calculate_route_location_with_negative_numbers():
    airports = [10, 2, -14, 7, 5]
    with pytest.raises(ValueError, match="Все числа должны быть положительными целыми числами."):
        calculate_route_location(airports)


def test_calculate_route_location_with_random_data():
    airports = [faker.random_int(min=0, max=10000) for _ in range(faker.random_int(min=1, max=1000))]
    expected_median = statistics.median(airports)
    assert calculate_route_location(airports) == expected_median
