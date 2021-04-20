
from TMA import TMA, Boy, Girl

def test_tma():
    side_a = [
        Boy("Adam", 0, [0, 1, 2]),
        Boy("Jack", 1, [1, 0, 2]),
        Boy("Tom", 2, [0, 1, 2])
    ]

    side_b = [
        Girl("Jessica", 0, [1, 2, 0]),
        Girl("Anna", 1, [0, 1, 2]),
        Girl("Margot", 2, [0, 1, 2])
    ]

    matching = TMA(optimal_side=side_b, wrost_side=side_a, amount_to_choose=1).run()

    print("Final Matching!")
    for boy, girl in matching:
        print("{} + {}".format(boy, girl))

if __name__ == "__main__":
    test_tma()