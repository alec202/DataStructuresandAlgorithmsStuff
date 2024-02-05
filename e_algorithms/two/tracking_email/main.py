stack = []
emails = int(input())
for i in range(emails):
    new = input()
    if new[0] == '1':
        level = new.split()[1]
        stack.append(int(level))
    if new[0] == '2':
        stack.pop()
    if new[0] == '3':
        print(max(stack))

