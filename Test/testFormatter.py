import unittest
import source.PostCodeResolver as val


class MyTestCase(unittest.TestCase):

    # happy paths
    def testValidFormat_Unformatted(self):
        resolver = val.PostCodeResolver()
        response = resolver.formatPostCode("EC1A1BB")
        self.assertEqual(0, response["errorCode"])
        self.assertEqual("EC1A 1BB", response["postCode"])

    def testValidFormat_Formatted(self):
        resolver = val.PostCodeResolver()
        response = resolver.formatPostCode("EC1A 1BB")
        self.assertEqual(0, response["errorCode"])
        self.assertEqual("EC1A 1BB", response["postCode"])

    # Sad paths/error cases
    def testInvalidCase_tooLong(self):
        resolver = val.PostCodeResolver()
        response = resolver.formatPostCode("EC1A1BBBB")
        self.assertEqual(1, response["errorCode"])
        self.assertEqual(1, len(response["errors"]))
        self.assertEqual(response["errors"][0], "given postcode is too long")

    def testInvalidCase_tooShort(self):
        resolver = val.PostCodeResolver()
        response = resolver.formatPostCode("EC1")
        self.assertEqual(1, response["errorCode"])
        self.assertEqual(1, len(response["errors"]))
        self.assertEqual(response["errors"][0], "given postcode is too short")

    def testInvalidCase_CannotBeFormatted(self):
        resolver = val.PostCodeResolver()
        response = resolver.formatPostCode("E11A11B")
        self.assertEqual(1, response["errorCode"])
        self.assertEqual(len(response["errors"]), 1)
        self.assertEqual(response["errors"][0], "given postcode cannot be formatted")


if __name__ == '__main__':
    unittest.main()
