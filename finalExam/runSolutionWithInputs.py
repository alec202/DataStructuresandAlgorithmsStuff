import writeToFile
from sortedList import MKAverage

def runner(commands: list[str], nums: list[int]):

    for command in commands:
        if command == "MKAverage":
            nums_for_m_and_k = nums.pop(0)
            mkObj = MKAverage(nums_for_m_and_k[0], nums_for_m_and_k[1])
        elif command == "addElement":
            newNum = nums.pop(0).pop()
            mkObj.addElement(newNum)
        elif command == "calculateMKAverage":
            print(mkObj.calculateMKAverage())
            nums.pop(0)


nums = writeToFile.parseNums()
commands = writeToFile.parseCommands()
runner(commands, nums)


