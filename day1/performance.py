from timeit import timeit
from v2 import preprocess_lines, sum_of_calibration_values


if __name__ == "__main__":
    iterations = 300
    lines = preprocess_lines()
    total_time = timeit(
        "sum_of_calibration_values(lines)", number=iterations, globals=globals()
    )
    print(f"Average time is {total_time * 1000 / iterations:.2f} ms")
