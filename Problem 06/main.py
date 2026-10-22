def find_word(sentences, word):
    count = 0
    positions = {}

    for i, sentence in enumerate(sentences):
        words = sentence.split()
        pos = -1

        for j, w in enumerate(words):
            if w == word:
                count += 1
                if pos == -1:
                    pos = j

        positions[i] = pos

    return count, positions


sentences = [
    "python is easy to learn",
    "I love python programming",
    "python is powerful",
    "I like programming"
]

word = "python"

count, positions = find_word(sentences, word)

print("Total occurrences:", count)
print("Positions:", positions)