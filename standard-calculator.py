
# TODO Add support for float inputs
# TODO Add support for parentheses
# TODO Add support for directly inputting roots (not to the power of a fraction)

# TODO Add support for simplifying expressions with variables

# TODO Add support for solving equations with variables


def organizeEquation(expression):
    outputExpression = []
    seperatorCharIndexList = []
    temporaryStringStorage = ""
    for i in enumerate(expression):
        index = i[0]
        char = i[1]
        try:
            int(char)
        except:
            seperatorCharIndexList.append(index)
    for i in enumerate(seperatorCharIndexList):
        listIndex = i[0]
        storedIndex = i[1]
        valueRangeIdentifier = listIndex - 1 > -1
        valueRangeFloor = 0
        if valueRangeIdentifier:
            valueRangeFloor = seperatorCharIndexList[listIndex - 1] + 1
        for j in range(valueRangeFloor, storedIndex):
            temporaryStringStorage += expression[j]
        outputExpression.extend([
            int(temporaryStringStorage),
            expression[storedIndex]
        ])
        temporaryStringStorage = ""
    for i in range(seperatorCharIndexList[-1] + 1, len(expression)):
        temporaryStringStorage += expression[i]
    outputExpression.append(int(temporaryStringStorage))
    return outputExpression


def operationFunction(sign, expression):
    while sign in expression:
        indexOfSign = expression.index(sign)
        valueOne = int(expression[indexOfSign - 1])
        valueTwo = int(expression[indexOfSign + 1])
        match sign:
            case '+':
                calculatedValue = valueOne + valueTwo
            case '-':
                calculatedValue = valueOne - valueTwo
            case '*':
                calculatedValue = valueOne * valueTwo
            case '/':
                calculatedValue = valueOne / valueTwo
            case '^':
                calculatedValue = valueOne ** valueTwo
        expression[indexOfSign - 1] = calculatedValue
        expression.pop(indexOfSign)
        expression.pop(indexOfSign)
    return expression


def doOperations(signs, expression):
    for i in enumerate(signs):
        sign = i[1]
        expression = operationFunction(sign, expression)
    return expression


# In the order of (P)EMDAS
operators = [
    '^',
    '*',
    '/',
    '+',
    '-'
]

inputEquation = input("Equation: ").replace(' ', '')
arrayEquation = list(inputEquation)

organizedEquation = organizeEquation(arrayEquation)
print(doOperations(operators, organizedEquation))
