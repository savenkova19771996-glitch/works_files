with open('input.txt', 'r', encoding='utf-8') as file:
    stroki = file.readlines()
    count = len(stroki)
    file.close()

with open('input.txt', 'r', encoding='utf-8') as file:
    k = file.readlines()
words_count = 0
for strok in k:
    words = strok.split()
    words_count += len(words)
    file.close()

with open('statistics.txt', 'w', encoding='utf-8') as file:
    file.write(f"Количество строк: {count}")
    file.write(f"\nОбщее количество слов: {words_count}")
    file.close()