"""
CP1404Practical
Word Occurrences Program
time estimate = 40 minutes
"""
word_to_count = {}
text = input("Text: ").split(" ")
text.sort()

print(text)

for word in text:
    count = text.count(word)
    word_to_count[word] = count

width = max(len(word) for word in list(word_to_count.keys()))

for word in word_to_count:
    print(f"{word:{width}} : {word_to_count[word]}")

