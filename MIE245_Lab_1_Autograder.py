import os
import importlib.util
import io
import contextlib
import pandas as pd


def test_case_1(module):
    points = 0
    total = 2

    # ground truth
    ground_truth = [1]
    ground_truth_print = ["1"]

    # build instance
    candidate_list = module.LinkedList()
    candidate_list.insert_start(1)

    # check build
    candidate_order = get_candidate_order(candidate_list)
    if candidate_order == ground_truth and candidate_list.tail.value == ground_truth[len(ground_truth)-1] and candidate_list.head.value == ground_truth[0]:
        points += 1

    # check print
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        candidate_list.print_linked_list()

    candidate_print = []
    for i in output.getvalue():
        candidate_print.append(str(i))
    candidate_print = sorted(candidate_print)[len(ground_truth_print):]
    if ground_truth_print == candidate_print:
        points += 1

    # return 1 if all tests passed
    if points == total:
        return 1

    # otherwise, return 0
    return 0


def get_candidate_order(linked_list):
    """ Iterates over linked list to get the order of elements. """
    current = linked_list.head
    candidate_order = []
    while current:
        candidate_order.append(int(current.value))
        current = current.next
    return candidate_order


def main():
    """ Evaluates all files in the submissions/ folder and saves to grade.csv. """
    path = "submissions" 
    files = list(os.listdir(path))

    print(files)

    all_grades = []
    for file in files:
        if 'MIE245_Lab_1_' in file:
            utorid = file[:-3].split("_")[-1]
            test_case_grades = [utorid]

            module_name = file.split("/")[-1].split(".")[0]
            module_path = path + "." + module_name
            print(module_path)
            module = importlib.import_module(module_path)

            try:
                test_case_grades.append(test_case_1(module))
            except:
                test_case_grades.append(0)

            print(test_case_grades)
            all_grades.append(test_case_grades)

    path_csv = "grades.csv"
    pd.DataFrame(all_grades).to_csv(path_csv, header = None, index = None)

if __name__ == '__main__':
    main()