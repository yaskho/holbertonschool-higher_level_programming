#!/usr/bin/python3
output = ""
for i in range(26):
    char = chr (97 + i)
if char not in ['q', 'e']:
    output += char
print(output, end='')
