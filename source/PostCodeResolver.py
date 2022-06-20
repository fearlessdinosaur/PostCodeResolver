# Validations and formatting based on https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
# as of 17/06/22
import re


class PostCodeResolver:
    # Hardcoded values as user should not expect to be able to set these.
    outwardCodeRegex = '^[A-Z]{1,2}[0-9][A-Z0-9]? '
    inwardCodeRegex = '[0-9][A-Z]{2}$'
    min_length = 6
    max_length = 8

    def validateLength(self, postcode, response):
        code_length = len(postcode)
        if code_length > self.max_length or code_length < self.min_length:
            if code_length > self.max_length:
                response["errors"].append("given postcode is too long")
            if code_length < self.min_length:
                response["errors"].append("given postcode is too short")

    def validateOutwardCode(self, postcode, response):
        matches = re.search(self.outwardCodeRegex, postcode)
        if matches is None:
            response["errors"].append("outward code invalid")
        return postcode

    def validateInwardCode(self, postcode, response):
        matches = re.search(self.inwardCodeRegex, postcode)
        if matches is None:
            response["errors"].append("inward code invalid")
        return postcode

    def getParts(self, postcode):
        # using the outward code regex with the space stripped to match unformatted strings
        outward_code = re.search(self.outwardCodeRegex[:-1], postcode)
        inward_code = re.search(self.inwardCodeRegex, postcode)

        codes = {
            "outwardCode": outward_code.group(0) if outward_code is not None else "",
            "inwardCode": inward_code.group(0) if inward_code is not None else ""
        }
        return codes

    def validatePostCode(self, postcode):
        response = self.buildResponse()
        self.validateLength(postcode, response)
        self.validateOutwardCode(postcode, response)
        self.validateInwardCode(postcode, response)

        if len(response["errors"]) > 0:
            response["errorCode"] = 1
        return response

    def formatPostCode(self, postcode):
        response = self.buildResponse()
        self.validateLength(postcode, response)

        if len(response["errors"]) == 0:
            parts = self.getParts(postcode)

            if parts["outwardCode"] != "" and parts["inwardCode"] != "":
                response["postCode"] = "{0} {1}".format(parts["outwardCode"], parts["inwardCode"])
            else:
                response["errorCode"] = 1
                response["errors"].append("given postcode cannot be formatted")
        else:
            response["errorCode"] = 1
        return response

    # Building the standard response
    def buildResponse(self):
        response = {
            "postCode": "",
            "errorCode": 0,
            "errors": []
        }
        return response
