import sys

if len(sys.argv) != 2:
    print("usage: python3 main.py <filename>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    is_safe_1 = is_safe_2 = 0
    for line in f:
        numbers = list(map(int, line.split()))
        if len(numbers) < 2:
            continue
        diffs = [b - a for a, b in zip(numbers, numbers[1:])]
        if all(1 <= d <= 3 for d in diffs) or all(1 <= -d <= 3 for d in diffs):
            is_safe_1 += 1
            is_safe_2 += 1
            continue
        for i in range(len(numbers)):
            temp_numbers = numbers[:i] + numbers[i + 1 :]
            temp_diffs = [b - a for a, b in zip(temp_numbers, temp_numbers[1:])]
            if all(1 <= d <= 3 for d in temp_diffs) or all(
                1 <= -d <= 3 for d in temp_diffs
            ):
                is_safe_2 += 1
                break

print(is_safe_1)
print(is_safe_2)
