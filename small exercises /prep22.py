def count_vowels(text, a, b):
    i = a
    count = 0
    while i <= b:
        char = text[i]
        if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
            count += 1
        i+= 1
    return count

print(count_vowels('one fish wasifeee two fish', 1, 20))
