"""..."""

import DataScienceBasics as dsb


def main():
    """..."""
    data = dsb.load_data('data.txt')
    new_data = [rec for rec in data if rec.get('score') != 100]
    for rec in new_data:
        rec['score'] -= 5

    scores = [rec['score'] for rec in new_data]
    stats = {
        'mean': dsb.calculate_mean(scores),
        'median': dsb.calculate_median(scores)
    }

    print("Unique player names: ", dsb.get_unique_values(new_data, 'name'))
    print(f"Mean score: {stats['mean']}")
    print(f"Median score: {stats['median']}")

    age_counts = {}
    for rec in new_data:
        age = rec.get('age')
        age_counts[age] = age_counts.get(age, 0) + 1

    print("Number of players by age:")
    for age, count in age_counts.items():
        print(f"Age {age}: {count}")


if __name__ == '__main__':
    main()
