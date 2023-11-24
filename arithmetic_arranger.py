def arithmetic_arranger(problems, showAnswer = False):
    arranged_problems = ""
    firstLine = ""
    secondLine = ""
    separator = ""
    answer = ""

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        number1, operation, number2 = problem.split()

        if operation not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if number1.isdigit() is not True or number2.isdigit() is not True:
            return "Error: Numbers must only contain digits."
        
        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        lengthDiference = max(len(number1), len(operation + " " + number2))

        if showAnswer:
            if operation == "+":
                answer += str(int(number1) + int(number2)).rjust(lengthDiference) + "    "
            else:
                answer += str(int(number1) - int(number2)).rjust(lengthDiference) + "    "
        

        firstLine += number1.rjust(lengthDiference) + "    "
        secondLine += operation + " " + number2.rjust(lengthDiference-2) + "    "
        separator += "-" * (lengthDiference) + "    "

    arranged_problems = firstLine + "\n" + secondLine + "\n" + separator + "\n" + answer

    return arranged_problems