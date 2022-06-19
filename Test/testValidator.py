import unittest
import source.postCodeValidator as val


class ValidatorTest(unittest.TestCase):

    # The 6 happy paths are based on the formats
    # given in https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation
    def testValidCase_Format1(self):
        output = val.validatePostCode("EC1A 1BB")
        print(output)
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format2(self):
        output = val.validatePostCode("A9A 9AA")
        print(output)
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format3(self):
        output = val.validatePostCode("A9 9AA")
        print(output)
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format4(self):
        output = val.validatePostCode("A99 9AA")
        print(output)
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format5(self):
        output = val.validatePostCode("AA9 9AA")
        print(output)
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format6(self):
        output = val.validatePostCode("AA99 9AA")
        print(output)
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    # Sad paths/error cases
    def testInvalidCase_DigitInAreaCode(self):
        output = val.validatePostCode("1C1A 1BB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "outward code Invalid")

    def testInvalidCase_NoDigitInDistrictCode(self):
        output = val.validatePostCode("ECAA 1BB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "outward code Invalid")

    def testInvalidCase_LetterInPostcodeSector(self):
        output = val.validatePostCode("EC1A ABB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "inward code Invalid")

    def testInvalidCase_NumberInPostcodeUnit(self):
        output = val.validatePostCode("EC1A 1B1")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "inward code Invalid")

    def testInvalidCase_MultipleErrors(self):
        output = val.validatePostCode("111A 11B")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 2)

    def testInvalidCase_TooLong(self):
        output = val.validatePostCode("EC1A 1BBA")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 2)
        self.assertEqual(output["errors"][0], "given postcode is too long")

    def testInvalidCase_TooShort(self):
        output = val.validatePostCode("EC1A ")
        self.assertEqual(1,output["errorCode"])
        self.assertEqual(len(output["errors"]), 2)
        self.assertEqual(output["errors"][0], "given postcode is too Short")

if __name__ == '__main__':
    unittest.main()
