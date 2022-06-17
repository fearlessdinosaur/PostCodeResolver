# Validations based on https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
# as of 17/06/22
import re

outwardCode = '^[A-Z]{1,2}[0-9][A-Z0-9]?'


def validateLength(postcode, response):
    codeLength = len(postcode)
    minlength = 6
    maxlength = 8
    if codeLength > maxlength or codeLength < minlength:
        if (codeLength > maxlength):
            response["errors"].append("given postcode is too long")
        if (codeLength < minlength):
            response["errors"].append("given postcode is too Short")


def validateOutwardCode(postcode, response):
    matches = re.search(outwardCode, postcode)
    if matches is None:
        response["errors"].append("outward code Invalid")
    return postcode


def validatePostCode(postcode):
    response = buildResponse()
    validateLength(postcode, response)
    validateOutwardCode(postcode, response)

    if len(response["errors"]) > 0:
        response["errorCode"] = 1
    return response


def buildResponse():
    response = {
        "postCode": "",
        "errorCode": 0,
        "errors": []
    }
    return response
