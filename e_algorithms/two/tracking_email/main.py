stack = {}
entry = 0
emails = int(input())
for i in range(emails):
    new = input()
    if new[0] == '1':
        level = int(new.split()[1])
        entry += 1
        stack[entry] = level

    elif new[0] == '2':
        entry -= 1

    elif new[0] == '3':
        print(max(stack.values()))

