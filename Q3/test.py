import loli_hex as hexlib
import unittest

class KnownValues(unittest.TestCase):
    knownValues = (
        (14, "E"),
        (16, "10"),
        (171,"AB"),
        (3452, "D7C"),
        (352, "160"),
        (15, "F"),
        (0, "0"),
        (1, "1"),
        (1234, "4D2"),
        (2781, "ADD"),
        (44252, "ACDC"),
        (65535, "FFFF"),
        (65536, "10000"),
        (1000, "3E8"),
        (789, "315"),
        (6940, "1B1C"),
        (255, "FF")
    )

    def testToHexValues(self):
        """toHex should give known result with known output"""
        for i, h in self.knownValues:
            result = hexlib.toHex(i)
            self.assertEqual(h, result)

class ToHexBadInput(unittest.TestCase):
    def testNegative(self):
        """toRoman should fail with negative input"""
        self.assertRaises(hexlib.InvalidArgument, hexlib.toHex, -1)

class CaseCheck(unittest.TestCase):
    def testToHexCase(self):
        """toHex should always return uppercase"""
        for i in range(0, 69420):
            numeral = hexlib.toHex(i)
            self.assertEqual(numeral, numeral.upper())

if __name__ == "__main__":
    unittest.main()
