to_do_list = [None] * 10

current_note = input()
while current_note != 'End':
    current_note_details = current_note.split('-')
    importance = int(current_note_details[0])
    note = current_note_details[1]
    to_do_list.insert(importance - 1, note)
    to_do_list.pop(importance)
    current_note = input()
print([x for x in to_do_list if x])
