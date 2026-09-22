# sentence = input("Enter a sentence: ")

# words = sentence.lower().split()

# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print("\nWord Frequency Count:")

# number = 1

# for word, count in word_count.items():
#     print(number, ".", word, "->", count)
#     number += 1



rows = int(input("Enter the number of rows: "))

print("\nTriangle Pattern:")

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nTriangle generation completed.")