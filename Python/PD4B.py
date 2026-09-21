sentence = input("Enter a sentence: ")

words = sentence.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency Count:")

number = 1

for word, count in word_count.items():
    print(number, ".", word, "->", count)
    number += 1