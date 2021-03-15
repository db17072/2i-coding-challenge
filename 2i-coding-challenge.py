
"""
-------------------
2i Coding Challenge
-------------------
By Danielle Bueno
13:00 - 14:00 Monday 15th March 2021
In Pyhton

In a language of your choice
could you please provide code that
iterates in multiples of 7 up until 100,
then in multiples of 8 up to 200, then
multiples of 9 up to 300.
"""
import unittest

# generator that iterates in multiples of n until max inclusive
def multiples(n,max):
    num = 0
    while num<=max:
        yield num
        num+=n

# prints generator outputs
def printMultiples(multGen):
    for i in multGen:
        print(i, end=", ")
    print("\n")

# returns generator outputs as list
def main(n,max):
    lstMultN_max = list(multiples(n,max))
    return lstMultN_max

# prints out list
def printMultiples(lstMult,n,max):
    print("Multiples of "+str(n)+" until "+str(max)+" inclusive:\r")
    for i in lstMult:
        print(i, end=", ")
    print("\n")

# --------------
# UNIT TESTS
# --------------

class allTests_TestCase(unittest.TestCase):

    def test_multiples(self):
        mult3_10 = multiples(3,10)
        self.assertEqual(next(mult3_10),0)
        self.assertEqual(next(mult3_10),3)
        self.assertEqual(next(mult3_10),6)
        self.assertEqual(next(mult3_10), 9)
        mult4_20 = multiples(4,20)
        self.assertEqual(next(mult4_20),0)
        self.assertEqual(next(mult4_20),4)
        self.assertEqual(next(mult4_20),8)
        self.assertEqual(next(mult4_20),12)
        self.assertEqual(next(mult4_20),16)
        self.assertEqual(next(mult4_20),20)

    def test_main(self):
        lst_mult3_10 = main(3,10)
        self.assertEqual(lst_mult3_10,[0,3,6,9])
        lst_mult4_20 = main(4,20)
        self.assertEqual(lst_mult4_20,[0,4,8,12,16,20])


if __name__ == '__main__':
    # multiples of 7 until 100 inclusive
    lst_mult7_100 = main(7,100)
    printMultiples(lst_mult7_100,7,100)
    # multiples of 8 until 200 inclusive
    lst_mult8_200 = main(8,200)
    printMultiples(lst_mult8_200,8,200)
    # multiples of 9 until 300 inclusive
    lst_mult9_300 = main(9,300)
    printMultiples(lst_mult9_300,9,300)
    # execute unit test
    unittest.main()
