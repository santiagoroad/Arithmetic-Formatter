# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

from arithmetic_arranger import arithmetic_arranger

# Error: Too many problems.
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 49", "123 + 49", "123 + 49"]))

# Error: Operator must be + or - .
print(arithmetic_arranger(["32 + 698", "3801 / 2", "45 * 43", "123 + 49"]))

# Error: Numbers cannot be more than four digits.
print(arithmetic_arranger(["32234 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Error: Numbers must only contain digits.
print(arithmetic_arranger(["3g2 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Good
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Run unit tests automatically
main(['-vv'])
