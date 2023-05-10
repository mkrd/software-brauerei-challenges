from challenge_01 import segment_array
from challenge_02 import find_missing_elements
from challenge_03 import sort_customers


def test_challenge_1():
    test_list = ["elem1", "elem2", "elem3", "elem4", "elem5", "elem6", "elem7"]
    assert segment_array(test_list, 3) == [
        ["elem1", "elem2", "elem3"],
        ["elem4", "elem5", "elem6"],
        ["elem7"]
    ]
    assert segment_array([], 2) == []
    assert segment_array(["1", "2"], 5) == [["1", "2"]]

def test_challenge_2():
    test_list = [
        ["elem1", "elem2", "elem3"],
        ["elem1", "elem2", "elem3", "elem4", "elem5", "elem6", "elem7"],
        ["elem2", "elem3"]
    ]
    assert find_missing_elements(test_list) == [
        ["elem1","elem4", "elem5", "elem6", "elem7"]
    ]
    assert find_missing_elements([["elem1", "elem1"], ["elem2"]]) == [["elem1", "elem2"]]
    assert find_missing_elements([["elem1", "elem2"], ["elem1"]]) == [["elem2"]]



def test_challenge_3():
    test_list = [
        {
            "customer_number": "1002442",
            "invoice": {
                "number": 850004111
            }
        },
        {
            "customer_number": "1352432",
            "invoice": {
                "number": 850002489
            }
        },
        {
            "customer_number": "1002442",
            "invoice": {
                "number": 850004391
            }
        },
        {
            "customer_number": "3944835",
            "invoice": {
                "number": 86028494
            }
        },
    ]

    assert sort_customers(test_list) == [
        {
            "customer_number": "1002442",
            "invoice": {
                "number": 850004391
            }
        },
        {
            "customer_number": "1002442",
            "invoice": {
                "number": 850004111
            }
        },
        {
            "customer_number": "1352432",
            "invoice": {
                "number": 850002489
            }
        },
        {
            "customer_number": "3944835",
            "invoice": {
                "number": 86028494
            }
        },
    ]


if __name__ == "__main__":
    test_challenge_1()
    test_challenge_2()
    test_challenge_3()
    print("All tests passed!")
