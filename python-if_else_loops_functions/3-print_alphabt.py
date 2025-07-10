#!/usr/bin/python3
print("{0}".format("".join([chr(c) for c in range(97,123) if c not in [101,113]])), end="")
