def main():
    num = int(input())
    genes = [int(i) for i in input().split()]
    start_prev = 0
    end_prev = 10000000000
    i = 0
    start_res = None
    end_res = None
    while (start_res == None or end_res ==None) and i <= num//2:
        if genes[i] > start_prev:
            start_prev = genes[i]
        else:
            start_res = i
        if genes[-(i+1)] < end_prev:
            end_prev = genes[i]
        else:
            end_res = i

        i+=1

    if (end_res+start_res == num-1):
        print('yes')
        print('swap', start_res, start_res+1) 
    elif genes[start_res:-end_res].sort() == genes[start_res:-end_res]:
        print("yes")
        print("reverse", start_res, num-end_res)
    if (end_res ==None and start_res == None):
        print("yes")

             


