sentence = input("Enter a sentence: ")
words = sentence.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("\nWord Frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")