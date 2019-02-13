# Homework 6: TSH Test Data Conversion
This repository was created on Feb 13th, 2019 for Duke BME547's sixth homework assignment.

## Usage
Please call this program in a terminal. 
- In Git BASH window, type ```python tsh.py```.
It will prompt nothing from the user.

## Output
```tsh.py``` will calculate whether or a person has: 
+ hyperthyroidism: any TSH value less than 1.0
+ hypothyroidism: any TSH value greater than 4.0
+ normal thyroid function: TSH values in between 1 and 4 (inclusive)

It saves a dictionary format of all the info corresponding to a person in a JSON file named by the person's name.
+ The data it retains in this dictionary is:
++ First Name
++ Last Name
++ Age
++ Gender
++ Diagnosis
++ TSH (containing a list of all of the test results)

These files are inside the folder 'Person JSON Files'

### Function
```tsh.py``` first reads every line of the test_data.txt file and makes a list of each line. It then removes the 'END' and the end of the list and then parses the list into a list of lists corresponding to each person and their attributes. 
+ This process contains a good amount of playing with the strings, including converting numbers to floats, sorting the TSH values (EXTRA CREDIT) and 

## Unit Testing
The ```test_tsh.py``` file contains parametrized tests that test each of the different realms that numbers could fall in for determining the diagnosis.

# Read The Docs (EXTRA CREDIT)
Documents have been created using Sphinx.
You will need to download the entire html folder which can be found 
+ [here](https://github.com/nicwainwright/bme547tsh/tree/master/docs/_build/html) 
+ or navigate to bme547tsh/docs/_build/html/ above