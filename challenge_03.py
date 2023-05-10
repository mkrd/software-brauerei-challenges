import argparse
import json


def sort_customers(customers: list[dict]) -> list[dict]:
    """
        Sorts a list of customers by customer number
        ascending and invoice number descending.
    """
    customers = sorted(customers, key=lambda c: c["invoice"]["number"], reverse=True)
    customers = sorted(customers, key=lambda c: int(c["customer_number"]))
    return customers


# Run the script from the command line with a file name(s) as argument(s)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_names", nargs="+")
    for file_name in parser.parse_args().file_names:
        with open(file_name, "r") as f:
            input_data = json.load(f)
        print(sort_customers(input_data))
