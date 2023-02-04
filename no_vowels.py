vowels = ['a', 'o', 'u', 'i', 'e', 'A', 'O', 'U', 'I', 'E']
list_without_vowels = [ x for x in input() if x not in vowels]
print(''.join(list_without_vowels))

