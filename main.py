# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

from arithmetic_arranger import arithmetic_arranger

# Error: Too many problems
# print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87']))

# print(arithmetic_arranger(["32 * 698", "3801 / 2", "45 + 43", "123 + 49"]))

# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print("aaaaaaaaaaaaaaaaaaa")
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Run unit tests automatically
main(['-vv'])
