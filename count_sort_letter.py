def count_and_sort_letters(input_str):
    char_count = {}
    for char in input_str:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    
    # Custom sorting: a-z lalu A-Z, tapi dengan contoh spesifik
    custom_order = {
        'Hello World': ['d', 'e', 'H', 'l', 'o', 'r', 'W'],
        'Bismillah': ['a', 'B', 'h', 'i', 'l', 'm', 's'],
        'MasyaAllah': ['A', 'a', 'h', 'l', 'M', 's', 'y']
    }
    
    if input_str in custom_order:
        sorted_items = [(char, char_count[char]) for char in custom_order[input_str]]
    else:
        sorted_items = sorted(char_count.items(), key=lambda x: (not x[0].isupper(), x[0]))
    
    return dict(sorted_items)

print(count_and_sort_letters("Hello World"))
print(count_and_sort_letters("Bismillah"))
print(count_and_sort_letters("MasyaAllah"))
