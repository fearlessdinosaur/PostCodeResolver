import unittest
import source.PostCodeResolver as Val


class ValidatorTest(unittest.TestCase):

    # The 6 happy paths are based on the formats
    # given in https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation
    def testValidCase_Format1(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("EC1A 1BB")
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format2(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("A9A 9AA")
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format3(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("A9 9AA")
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format4(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("A99 9AA")
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format5(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("AA9 9AA")
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    def testValidCase_Format6(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("AA99 9AA")
        self.assertEqual(output["errorCode"], 0)
        self.assertEqual(len(output["errors"]), 0)

    # Sad paths/error cases
    def testInvalidCase_DigitInAreaCode(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("1C1A 1BB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "outward code invalid")

    def testInvalidCase_NoDigitInDistrictCode(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("ECAA 1BB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "outward code invalid")

    def testInvalidCase_LetterInPostcodeSector(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("EC1A ABB")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "inward code invalid")

    def testInvalidCase_NumberInPostcodeUnit(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("EC1A 1B1")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 1)
        self.assertEqual(output["errors"][0], "inward code invalid")

    def testInvalidCase_MultipleErrors(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("111A 11B")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 2)

    def testInvalidCase_TooLong(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("EC1A 1BBA")
        self.assertEqual(output["errorCode"], 1)
        self.assertEqual(len(output["errors"]), 2)
        self.assertEqual(output["errors"][0], "given postcode is too long")

    def testInvalidCase_TooShort(self):
        resolver = Val.PostCodeResolver()
        output = resolver.validatePostCode("EC1A ")
        self.assertEqual(1, output["errorCode"])
        self.assertEqual(len(output["errors"]), 2)
        self.assertEqual(output["errors"][0], "given postcode is too short")


if __name__ == '__main__':
    unittest.main()
