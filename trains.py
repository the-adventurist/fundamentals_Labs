number_of_wagons = int(input())
wagons = [0] * number_of_wagons

command = input()

while command != 'End':
    command_args = command.split()
    action = command_args[0]
    if action == 'add':
        people_to_add = int(command_args[1])
        wagons[-1] += people_to_add
    elif action == 'insert':
        index = int(command_args[1])
        people_to_add = int(command_args[2])
        wagons[index] += people_to_add
    elif action == 'leave':
        index = int(command_args[1])
        people_to_leave = int(command_args[2])
        wagons[index] -= people_to_leave
    command = input()
print(wagons)
