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
        person[3] = person[3][4:]
        
        # create float valued TSH list for each person
        person[3] = person[3].split(',')
        person[3] = [float(i) for i in person[3]]
        # turn ages into integers
        person[1] = int(person[1])
        
        personList.append(person)
    return personList


def getDiagnosis(tshList):
    """Finds whether a person has hypo/hyper thyroidism
    
    Uses a max and min to determine if a person's TSH tests pass
    
    Args:
        tshList: the component of peopleList that contains float tsh values
    
    Returns:
        condition: string that says "hyperthyroidism" 
        as defined by any of their tests results being less than 1.0,
        "hypothyroidism" as defined by any of their test results being greater
        than 4.0, or"normal thyroid function" as defined by all of their test
        results being between 1.0 and 4.0, inclusive.
        
    """
    if min(tshList) < 1.0:
        condition = "hyperthyroidism"
    elif max(tshList) > 4.0:
        condition = "hypothyroidism"
    else:
        condition = "normal thyroid function"
    
    return condition

#def main():
big_list = readFile()
peopleList = parsePeopleList(big_list)
print(peopleList)
print(getDiagnosis(peopleList[0][3]))
# if __name__ == "__main__":
 #   main()
