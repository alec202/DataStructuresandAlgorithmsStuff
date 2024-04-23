import pandas as pd
import numpy as np
import csv
import json

def parseCommands():
    # Open the file in read mode
    with open("testCase13Commands.txt", "r") as file:
        # Read all lines into a list
        lines = file.readlines()

    # Initialize an empty list to store commands

    # Iterate over each line
    for line in lines:
        # Split the line into individual commands
        line_commands = line.strip().split(",")

    for index, command in enumerate(line_commands):
        stripped_command = command.strip('"')
        line_commands[index] = stripped_command

# use print statement below to write to the file using:
    # write_to_csv(parseCommands(), "strippedTestCase13Commands.txt")
    # return [line_commands]

    # otherwise can just return line_commands
    return line_commands


def write_stuff(stuff_to_write):
    with open("strippedTestCase13Commands.txt", "w") as file:
        csv.writer()
        file.writelines(stuff_to_write)

def write_to_csv(data, filename):
    # Create a DataFrame from the array
    df = pd.DataFrame(data)

    # Write the DataFrame to a CSV file
    df.to_csv(filename, index=False, header=False)

def parseNums():

    # read data
    with open("testCase13Nums.txt", "r") as file:
        data_str = file.read()
    # Parse the string into a Python list
    data_list = json.loads(data_str)

    return data_list

if __name__ == "__main__":
    print(parseCommands())
    # write_to_csv(parseCommands(), "strippedTestCase13Commands.txt")
    # parseNums()