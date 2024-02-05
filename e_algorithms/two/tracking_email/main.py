import heapq
def main():
    heap = []
    #heapq.heapify(heap)
    stack = {}
    entry = 0
    emails = int(input())
    for i in range(emails):
        new = input()
        if new[0] == '1':
            level = int(new.split()[1])
            entry += 1
            stack[entry] = level
            heapq.heappush(heap, -1*level)

        elif new[0] == '2':
            heap.remove(-1*(stack[entry]))
            heapq.heapify(heap)
            stack[entry] = 0
            entry -= 1

        elif new[0] == '3':
            print(-1*heap[0])

if __name__ == "__main__":
    main()
