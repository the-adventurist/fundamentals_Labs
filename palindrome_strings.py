words = input().split()
palindrome_word = input()
print([word for word in words if word == word[::-1]])
times_word_occurs = len([+1 for word in words if word == palindrome_word])
print(f"Found palindrome {times_word_occurs} times")
