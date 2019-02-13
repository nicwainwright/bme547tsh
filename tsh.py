# -*- coding: utf-8 -*-
"""
Created on Feb 13

@author: nicwainwright

BME547 Homework 5
TSH Test Data Conversion
"""
import json


def readFile():
    """ Read the test_data.txt file into a large list

    Returns:
        list: a list of every data entry
    """
    file = open("test_data.txt", "r")
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

        # sort the float values of each person's TSH scores
        person[3] = sorted(person[3])

        # turn ages into integers
        person[1] = int(person[1])

        # add the person to the list of people
        personList.append(person)
    return personList


def getDiagnosis(tshList):
    """Finds whether a person has hypo/hyper thyroidism

    Uses a max and min to determine if a person's TSH tests pass or fail for
    hypo or "hyperthyroidism" as defined by any of their tests results being
    less than 1.0, "hypothyroidism" as defined by any of their test results
    being greater than 4.0, or"normal thyroid function" as defined by all of
    their test results being between 1.0 and 4.0, inclusive.

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


def makePersonDict(person):
    """Turn a list of a person's values into a dictionary

    Args:
        person (list): a list representation of a person after it has been
        parsed appropriately

    Returns:
        dictionary: a dictionary that includes separated names and diagnosis
    """
    names = person[0].split(' ')
    diagnosis = getDiagnosis(person[3])
    dictionary = {"First Name": names[0], "Last Name": names[1],
                  "Age": person[1], "Gender": person[2],
                  "Diagnosis": diagnosis, "TSH": person[3]}
    return dictionary


def saveToJSON(personDict):
    """Save a person to a JSON

    Args:
        personDict (dict): a dictionary of the values corresponding to one
        person

    Returns:
        nothing: but saves a JSON file for the person
    """
    first = personDict.get("First Name")
    last = personDict.get("Last Name")
    filename = first + "-" + last + ".json"
    outfile = open(filename, "w")
    json.dump(personDict, outfile)
    outfile.close()


def main():
    """Main function that saves JSON files for number of people in test_data

    Args:

    Returns:
        Nothing: but does save JSONs through calling of saveToJSON function
    """
    full_list = readFile()
    people_list = parsePeopleList(full_list)
    for i in range(len(people_list)):
        saveToJSON(makePersonDict(people_list[i]))


if __name__ == "__main__":
    main()
