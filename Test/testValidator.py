import unittest
import source.postCodeValidator as val


class ValidatorTest(unittest.TestCase):

    def testValidCase(self):
        output = val.validatePostCode("EC1A 1BB")
        print(output)
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

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
        output = val.validatePostCode("EC1A 1BB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "inward code Invalid")

    def testInvalidCase_NumberInPostcodeUnit(self):
        output = val.validatePostCode("EC1A 1BB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "inward code Invalid")

    def testInvalidCase_MultipleErrors(self):
        output = val.validatePostCode("EC1A 1BB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "inward code Invalid")

    def testInvalidCase_TooLong(self):
        output = val.validatePostCode("EC1A 1BBA")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 2)
        self.assertEqual(output["errors"][0], "given postcode is too long")

    def testInvalidCase_TooShort(self):
        output = val.validatePostCode("EC1A ")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 2)
        self.assertEqual(output["errors"][0], "given postcode is too Short")
