# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells.
# Output: 13

list_t = (input('Введите текст: ').lower().replace('.', ' ').split())
print(list_t)
set_list_t = set()
for i in list_t:
    set_list_t.add(i)
print(len(set_list_t))

print(len(set(input('Введите текст ').upper().replace('.', ' ').split())))
