import heapq

if __name__ == "__main__":

    #https://stackoverflow.com/questions/10162679/python-delete-element-from-heap

    def remove(number, first_heap, second_heap):
        if number not in first_heap or number not in second_heap:
            print("Wrong!")

        if number <= 



    def add(number,first_heap, second_heap):
        heapq.heappush(first_heap,number)
        heapq.heappush(second_heap,number)

    number_of_tests = int(input())
    first_half_heap = []
    second_half_heap = []



    for tests in range(number_of_tests):
        current_line = input().split()

        operation = current_line[0]
        number = current_line[1]

        if operation == "r":
            remove(number, first_half_heap, second_half_heap)
        else:
            add(number,first_half_heap,second_half_heap)

        

