def find_name(wordlist, name):
    count = 0
    positions = []

    for word in wordlist:
        index = word.find(name)

        if index != -1:
            count += 1
            positions.append(index)
        else:
            positions.append(0)

    return (count, positions)


# Example
wordlist = ["abhay", "hello", "abhayvijayan", "python"]
name = "abhay"

result = find_name(wordlist, name)
print(result)