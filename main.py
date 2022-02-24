def deleteArrayItems(arr, deletedChar):
    for i, char in enumerate(arr):
        if char == deletedChar:
            del arr[i]
    return arr


def operatorDetection(arr):
    for i, value in enumerate(arr):
        match value:
            case '+':
                operator = '+'
            case '-':
                operator = '-'
            case _:
                continue
        if i - 1 >= 0 & i + 1 <= len(arr):
            index1 = i - 1
            index2 = i + 1
        else:
            continue
        if not ((type(arr[index1]) == int) & (type(arr[index2]) == int)):
            continue
        return [operator, index1, index2]
    return False


def addFunction(positions, equation):
    pos1 = equation[positions[1]]
    pos2 = equation[positions[2]]
    if positions[0] != '+':
        print("There was an error when processing the addition.")
        exit()
    print(type(pos1), type(pos2))
    if isinstance(pos1, int) & isinstance(pos2, int):
        return pos1 + pos2
    else:
        print('no class found')


input = input('Equation - ')  # "X + X = 4"
equation = deleteArrayItems(list(input), ' ')

# convert numbers to integers if possible
for i in range(len(equation)):
    try:
        equation[i] = int(equation[i])
    except:
        pass

print(''.join(str(char) for char in equation))

while True:
    operations = operatorDetection(equation)
    print(operations)
    if not operations:
        break
    addedNum = addFunction(operations, equation)

    for i in range(3):
        equation.pop(operations[1])
    equation.insert(operations[1], addedNum)
    print(equation)
