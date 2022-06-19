import unittest
import source.postCodeValidator as val


class MyTestCase(unittest.TestCase):

    def testValidFormat_Unformatted(self):
        response = val.formatPostCode("EC1A1BB")
        self.assertEqual(0, response["errorCode"])
        self.assertEqual("EC1A 1BB", response["postCode"])

    def testValidFormat_Formatted(self):
        response = val.formatPostCode("EC1A 1BB")
        self.assertEqual(0, response["errorCode"])
        self.assertEqual("EC1A 1BB", response["postCode"])


    def testInvalidCase_tooLong(self):
        response = val.formatPostCode("EC1A1BBBB")
        self.assertEqual(1, response["errorCode"])
        self.assertEqual(1, len(response["errors"]))
        self.assertEqual(response["errors"][0], "given postcode is too long")

    def testInvalidCase_tooShort(self):
        response = val.formatPostCode("EC1")
        self.assertEqual(1, response["errorCode"])
        self.assertEqual(1,len(response["errors"]))
        self.assertEqual(response["errors"][0], "given postcode is too Short")

    def testInvalidCase_CannotBeFormatted(self):
        response = val.formatPostCode("E11A11B")
        self.assertEqual(1, response["errorCode"])
        self.assertEqual(len(response["errors"]), 1)
        self.assertEqual(response["errors"][0], "given postcode cannot be formatted")


if __name__ == '__main__':
    unittest.main()
