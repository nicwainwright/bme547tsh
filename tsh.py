# -*- coding: utf-8 -*-
"""
Created on Feb 13

@author: nicwainwright

BME547 Homework 5
TSH Test Data Conversion
"""

def readFile():
    """ Read the test_data.txt file into a large list
    
    Returns:
        list: a list of every data entry
    
    """
    file = open("test_data.txt","r")
    lines = file.read().splitlines()
    file.close()
    # delete 'END' entry
    del lines[len(lines)-1]
    return lines

def separatePeopleList(big_list):
    personList = []
    for i in range(0, len(big_list), 4):
        person = big_list[i:i+4]
        personList.append(person)
    return personList


#def main():
big_list = readFile()
peopleList = separatePeopleList(big_list)
print(peopleList)
# if __name__ == "__main__":
 #   main()
