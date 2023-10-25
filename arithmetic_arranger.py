def arithmetic_arranger(problems):
    arranged_problems = ""
    arranged_problems1 = ''
    arranged_problems2 = ''
    arranged_problems3 = ''

    # Validates if there are too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for i in range (len(problems)):
        operation = problems[i]
        infooperation = operation.split()

        # Validates if the values are just numbers, else error
        try:
            int(infooperation[0])
            int(infooperation[2])
        except:
            return 'Error: Numbers must only contain digits.'
        
        # Validates if the operation are allowed
        if infooperation[1] == '*' or infooperation[1] == '/':
            return 'Error: Operator must be + or - .'
        # Validates the digits of the numbers
        elif len(infooperation[0]) > 4 or len(infooperation[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        # Begin the construncion of the answer
        else:
            # Put the logic to order the information
            arranged_problems1 = arranged_problems1 + infooperation[0]
            arranged_problems2 = arranged_problems2 + infooperation[1]
            arranged_problems3 = arranged_problems3 + infooperation[2]

            arranged_problems1 = arranged_problems1 + '/'
            arranged_problems2 = arranged_problems2 + '/'
            arranged_problems3 = arranged_problems3 + '/'
    
    print(arranged_problems1)
    print(arranged_problems2)
    print(arranged_problems3)
    
    return arranged_problems