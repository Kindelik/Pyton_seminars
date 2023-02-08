# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход
# подается только одно слово, которое содержит либо только английские, либо только русские буквы.

dictX = \
    {1: "AEIOULNSTRАВЕИНОРСТ",
     2: "DGДКЛМПУ",
     3: "BCMPБГЁЬЯ",
     4: "FHVWYЙЫ",
     5: "KЖЗХЦЧ",
     8: "JXШЭЮ",
     10: "QZФЩЪ"
     }
strX = input("введите слово: ").upper()
scores = 0
for ch in strX:
    for key, val in dictX.items():
        if ch in val:
            scores += key
            break

print(scores)
