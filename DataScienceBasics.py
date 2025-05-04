"""..."""

import json


def calculate_mean(numbers):
    """calculates the mean of a list of numbers"""
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """calculates the median of a list of numbers"""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2


def load_data(filename):
    """loads data from a file where each line is a json object"""
    data = []
    f = open(filename, 'r', encoding='utf-8')
    try:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data.append(json.loads(line))
    finally:
        f.close()
    return data


def filter_data(dataset, condition):
    """filters a dataset using a condition"""
    return [item for item in dataset if condition(item)]


def get_unique_values(dataset, key):
    """extracts unique values for a specified key from the dataset"""
    return {item[key] for item in dataset if key in item}


def transform_data(dataset, key, transform):
    """applies a transformation function into a specific key in each item
    of the dataset"""
    transformed = []
    for item in dataset:
        if key in item:
            new_item = item.copy()
            new_item[key] = transform(new_item[key])
            transformed.append(new_item)
        else:
            transformed.append(item.copy())
    return transformed


def describe_data(dataset, key):
    """prints the mean and median for a specific key in the dataset"""
    values = [item[key] for item in dataset if key in item]
    if not values:
        print(f"No data found for key '{key}'.")
        return
    mean_value = calculate_mean(values)
    median_value = calculate_median(values)

    print(f"Mean of '{key}': {mean_value}")
    print(f"Median of '{key}': {median_value}")


def aggregate_data(dataset, group_key, value_key):
    """aggregates numeric values by group"""
    aggregation = {}
    for item in dataset:
        if group_key in item and value_key in item:
            key_val = item[group_key]
            aggregation[key_val] = (
                aggregation.get(key_val, 0) + item[value_key]
            )
    return aggregation
