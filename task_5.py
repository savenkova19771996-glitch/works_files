words = []

with open("words.txt", "r", encoding="utf-8") as infile:
    for line in infile:
        words.append(line.strip())

words_alfavit = sorted(words)

words_length = sorted(words, key = len)

words_reverse = sorted(words, reverse = True)

with open("orted_alphabetically.txt", "w", encoding="utf-8") as outfile:
    for word in words_alfavit:
        outfile.write(word + "\n")

with open("sorted_by_length.txt", "w", encoding="utf-8") as outfile:
    for word in words_length:
        outfile.write(word + "\n")

with open("sorted_reverse.txt", "w", encoding="utf-8") as outfile:
    for word in words_reverse:
        outfile.write(word + "\n")

print("файлы созданы")
