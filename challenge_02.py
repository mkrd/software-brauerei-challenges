import argparse
import json


def find_missing_elements(array: list[list[str]]) -> list[str]:
    """
        Find the elements that are missing from at least one sub-array.
    """
    # Count in how many sub-arrays each element occurs
    occurences = {}  # {elem: count}
    for sub_array in array:
        for ele in set(sub_array):
            occurences[ele] = occurences.get(ele, 0) + 1
    # Filter out elements that occur in all sub-arrays
    res = [ele for ele, count in occurences.items() if count < len(array)]
    return [list(sorted(res))]


# Run the script from the command line with a file name(s) as argument(s)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_names", nargs="+")
    for file_name in parser.parse_args().file_names:
        with open(file_name, "r") as f:
            input_data = json.load(f)
        print(find_missing_elements(input_data))
