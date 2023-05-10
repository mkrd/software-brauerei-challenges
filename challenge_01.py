import argparse
import json


def segment_array(array: list[str], size: int) -> list[list[str]]:
    """
        Segment an array into sub-arrays of a given size.
        The last segment can be smaller than the given size.
    """
    segment_count, last_segment_size = divmod(len(array), size)

    res = []
    for i in range(segment_count):
        res.append(array[i * size : (i + 1) * size])

    if last_segment_size > 0:
        res.append(array[-last_segment_size:])

    return res


# Run the script from the command line with a file name(s) as argument(s)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_names", nargs="+")
    for file_name in parser.parse_args().file_names:
        with open(file_name, "r") as f:
            input_data = json.load(f)
        print(segment_array(input_data, 3))
