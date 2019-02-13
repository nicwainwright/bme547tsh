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


def parsePeopleList(big_list):
    """Get a lists of lists where sublists are a person and their info
    
    Args:
        big_list: a master list which is just a test_data.txt file read in
        
    Return:
        personList: a lists of lists of people and their info
    """
    personList = []
    for i in range(0, len(big_list), 4):
        person = big_list[i:i+4]
        # omit "TSH" from each tsh list
        person[len(person)-1] = person[len(person)-1][4:]
        # turn ages into integers
        person[1] = int(person[1])
        personList.append(person)
    return personList


def getDiagnosis():
    """Finds whether a person has hypo/hyper thyroidism
    
    Uses a max and min to determine if a person's TSH tests pass
    
    Args:
        
    """
    


#def main():
big_list = readFile()
peopleList = parsePeopleList(big_list)
print(peopleList)
# if __name__ == "__main__":
 #   main()