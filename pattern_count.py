def pattern_count(text, pattern):
    if not pattern or len(pattern) > len(text):
        return 0
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

print(pattern_count("palindrom", "ind"))  # 1
print(pattern_count("abakadabra", "ab"))  # 2
print(pattern_count("hello", ""))  # 0
print(pattern_count("ababab", "aba"))  # 2
print(pattern_count("aaaaaa", "aa"))  # 5
print(pattern_count("hell", "hello"))  # 0