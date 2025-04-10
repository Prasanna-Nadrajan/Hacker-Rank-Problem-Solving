from itertools import combinations

length = int(input())
letters = input().split()
num_selected = int(input())

indices = list(range(length))
all_combinations = list(combinations(indices, num_selected))

favorable_count = 0
for combo in all_combinations:
    if any(letters[i] == 'a' for i in combo):
        favorable_count += 1

total_combinations = len(all_combinations)
probability = favorable_count / total_combinations

print(probability)
