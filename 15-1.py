#!/usr/bin/env python3

def hash_string(s: str) -> int:
    Hash = 0
    for c in s:
        Hash += ord(c)
        Hash = (Hash * 17) % 256
    return Hash

with open('in.15', 'r') as fd:
    line = fd.read()

# Remove newline
line = line[:-1]

# Split by ,
hashes = line.split(',')

result = 0
for Hash in hashes:
    result += hash_string(Hash)

print(result)
