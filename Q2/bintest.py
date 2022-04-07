import binsearch as bsearch
import unittest
import random

# class KnownValues(unittest.TestCase):
#     knownValues = (((10,20,30), 20), 1), (((10,20,30), 30), 2)

class SanityCheck(unittest.TestCase):
    def testIInNLength(self):
        l = []
        for i in range(10,11,1):
            dataList = [j for j in range(i-10, i)]
            idx = random.randint(0,9)
            value = dataList[idx]
            l.append(((dataList,dataList[idx]), idx))
        i = bsearch.binsearch(dataList, value)
        print(i)
        print(len(dataList))
        self.assertLessEqual(i, len(dataList))
    def testvalueEqualKey(self):
        l = []
        for i in range(10,11,1):
            dataList = [j for j in range(i-10, i)]
            idx = random.randint(0,9)
            value = dataList[idx]
            l.append(((dataList,dataList[idx]), idx))
            i = bsearch.binsearch(dataList, value)
            self.assertEqual(value, dataList[idx])
    def testreturnNone(self):
        l = []
        for i in range(10,11,1):
            dataList = [j for j in range(i-10, i)]
            idx = random.randint(0,9)
            value = dataList[idx]
            l.append(((dataList,dataList[idx]), idx))
            i = bsearch.binsearch(dataList, value)
            if i == "None":
                self.assertGreater(i, len(dataList))


if __name__=="__main__":
    unittest.main()
