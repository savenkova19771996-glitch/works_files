search_word = input("Введите слово для поиска: ").strip()
search_wordlower = search_word.lower()

num_lines = []
total_count = 0


with open('text.txt', 'r', encoding='utf-8') as file:

    for k, line in enumerate(file, start=1):
        line_lower = line.lower()
        count_line = line_lower.count(search_wordlower)

        if count_line > 0:
            total_count += count_line

            num_lines.append(k)

if total_count > 0:
    j = "Да"
else:
    j = "Нет"

print(f"Слово найдено: {j}")
print(f"Сколько раз оно встречается: {total_count}")
print(f"В каких строках встречается: {num_lines}")

with open("search_results.txt", "w", encoding="utf-8") as output:
    output.write(f"Введённое слово: {search_word}")
    output.write(f"\nСлово найдено: {j}")
    output.write(f"\nСколько раз оно встречается: {total_count}")
    output.write(f"\nВ каких строках встречается: {num_lines}")