def main():
    num = int(input())
    sgenes = [int(i) for i in input().split()]
    genes = [i for i in sgenes]
    sgenes.sort()
    wrongs = []
    for i in range(num):
        if genes[i] != sgenes[i]:
            wrongs.append(i)
    ##print(wrongs)
    if len(wrongs) == 0:
        print("yes")
    elif len(wrongs) == 2:
        print("yes")
        print("swap", wrongs[0]+1, wrongs[1]+1)
    else:
        chunk = genes[wrongs[0]: wrongs[-1]+1]
        sorted_chunk = [j for j in chunk]
        sorted_chunk.sort(reverse = True)
        if chunk == sorted_chunk:
            ##print(genes[wrongs[0]: wrongs[-1]+1])
            ##print(genes[wrongs[0]: wrongs[-1]+1].sort())
            print("yes")
            print("reverse", wrongs[0]+1, wrongs[-1]+1)
        else:
            print('no')
main()

             


