employees = [int(x) for x in input().split()]
happiness_factor = int(input())
levels_of_happiness = [x * happiness_factor for x in employees]
general_threshold = sum(levels_of_happiness) / len(levels_of_happiness)
happy_employees = [+1 for x in levels_of_happiness if x > general_threshold]
if len(happy_employees) >= len(levels_of_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(levels_of_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(levels_of_happiness)}. Employees are not happy!")
