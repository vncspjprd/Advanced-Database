def frequency(s):
    freq = {}
    for char in s:
        if char != ' ':
            freq[char] = freq.get(char, 0) + 1
    return freq

user_input = input("Enter string: ")
strings = [s.strip() for s in user_input.split(",")]

for s in strings:
    freq = frequency(s)
    output = ', '.join([f"{k}={v}" for k, v in freq.items()])
    print(output)