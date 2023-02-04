numbers = [int(x) for x in input().split(', ')]
searched_indexes = [i for i, x in enumerate(numbers) if x % 2 == 0]
print(searched_indexes)
