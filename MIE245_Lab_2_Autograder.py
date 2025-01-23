import os
import importlib.util
import io
import contextlib
import pandas as pd

"""
Instructions: 
- Place this file in the same directory as the submissions folder.
- Run this file to generate the grades.csv file.
- The grades.csv file will contain the utorid and grade for each student.
- The grade is 1 if the student passes all test cases, and 0 otherwise.
- The test_case_1 function is an example of how to write test cases.
- You can add more test cases by defining additional test_case_* functions.
- You can also modify the main function to include additional test cases.
- The test_case_* functions should return 1 if the student passes the test case, and 0 otherwise.

Current directory should be structured as follows:
|- MIE245_Lab_2_Autograder.py
|- submissions
    |- MIE245_Lab_2_Template_<UTORID>.py
"""
# Define a helper function to test sorting methods
def test_sort_method(cls, method_name, input_list, ground_truth):
    try:
        method = getattr(cls, method_name)
        return 1 if method(input_list) == ground_truth else 0
    except Exception as e:
        return 0
    
def test_case_1(module):
    points = []
    
    # Specify input and ground truth
    input_list = [0, 5, -10, 10, -5]
    ground_truth = [10, 5, 0, -5, -10]    
    
    # call instance
    try:
        sort_util = module.SortUtility()
    except Exception as e:
        return [0, 0]
    
    # Test insertion_sort and merge_sort methods
    points.append(test_sort_method(sort_util, 'insertion_sort', input_list.copy(), ground_truth))
    points.append(test_sort_method(sort_util, 'merge_sort', input_list.copy(), ground_truth))
    
    return points


def main():
    """ Evaluates all files in the submissions/ folder and saves to grade.csv. """
    path = "submissions" 
    files = list(os.listdir(path))

    all_grades = []
    for file in files:
        if 'MIE245_Lab_2_' in file:
            utorid = file[:-3].split("_")[-1]
            test_case_grades = [utorid]

            module_name = file.split("/")[-1].split(".")[0]
            module_path = path + "." + module_name

            module = importlib.import_module(module_path)

            test_case_grades.extend(test_case_1(module))
            
            # Add another test case here
            # try:
            #     test_case_grades.append(test_case_2(module))
            # except:
            #     test_case_grades.append(0)


            all_grades.append(test_case_grades)

    path_csv = "grades.csv"
    pd.DataFrame(all_grades).to_csv(path_csv, header = None, index = None)


if __name__ == '__main__':
    main()

