arr = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]
letters = sorted([x for x in arr if isinstance(x, str)])
numbers = sorted([x for x in arr if isinstance(x, int)])
result = letters + numbers
print(result)

# hasil ['A', 'B', 'J', 'M', 'N', 9, 12, 30, 82, 99]     