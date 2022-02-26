
# TODO Add support for parentheses
# TODO (maybe) Add support for directly inputting roots (instead of "to the power of a fraction")

# TODO Add support for simplifying expressions with variables

# TODO Add support for solving equations with variables

def organizeEquation(expression):
    if len(expression) == 1:
        return expression
    outputExpression = []
    seperatorCharIndexList = []
    temporaryStringStorage = ''
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
        valueRangeIdentifier = listIndex > 0
        valueRangeFloor = 0
        if valueRangeIdentifier:
            valueRangeFloor = seperatorCharIndexList[listIndex - 1] + 1
        for j in range(valueRangeFloor, storedIndex):
            temporaryStringStorage += expression[j]
        if temporaryStringStorage == '':
            temporaryStringStorage = '0'
        outputExpression.extend([
            int(temporaryStringStorage),
            expression[storedIndex]
        ])
        temporaryStringStorage = ''
    for i in range(seperatorCharIndexList[-1] + 1, len(expression)):
        temporaryStringStorage += expression[i]
    if temporaryStringStorage == '':
        temporaryStringStorage = '0'
    outputExpression.append(int(temporaryStringStorage))
    return outputExpression


def operations(sign, expression):
    while sign in expression:
        indexOfSign = expression.index(sign)
        valueOne = expression[indexOfSign - 1]
        valueTwo = expression[indexOfSign + 1]
        match sign:
            case '.':
                if not isinstance(valueOne, int):
                    valueOne = 0
                calculatedValue = float(str(valueOne) + "." + str(valueTwo))
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
        if calculatedValue % 1 == 0.0:
            calculatedValue = int(calculatedValue)
        expression[indexOfSign - 1] = calculatedValue
        expression.pop(indexOfSign)
        expression.pop(indexOfSign)
    return expression


def doAllOperations(signs, expression):
    for sign in signs:
        expression = operations(sign, expression)
    return expression


# In the order of (P)EMDAS plus decimals
operators = [
    '.',
    '^',
    '*',
    '/',
    '+',
    '-'
]

inputEquation = input("Equation: ").replace(' ', '')
arrayEquation = list(inputEquation)
organizedEquation = organizeEquation(arrayEquation)
print(doAllOperations(operators, organizedEquation)[0])
