def main():
    vals = input()
    reps = int(vals.split()[0])
    plans = int(vals.split()[1])
    sort = [0 for j in range(plans)]
    for i in range(reps):
        new = int(input())
        for index in range(len(sort)):
            if new > sort[index]:
                sort.insert(index, new)
                sort = sort[0:plans]
                break
    for val in sort:
        print(val)
main()
