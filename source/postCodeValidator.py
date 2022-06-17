# Validations based on https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
# as of 17/06/22
import re

outwardCode = '^[A-Z]{1,2}[0-9][A-Z0-9]? '
inwardCode = '[0-9][A-Z]{2}$'
min_length = 6
max_length = 8


def validateLength(postcode, response):
    code_length = len(postcode)
    if code_length > max_length or code_length < min_length:
        if code_length > max_length:
            response["errors"].append("given postcode is too long")
        if code_length < min_length:
            response["errors"].append("given postcode is too Short")


def validateOutwardCode(postcode, response):
    matches = re.search(outwardCode, postcode)
    if matches is None:
        response["errors"].append("outward code Invalid")
    return postcode


def validateInwardCode(postcode, response):
    matches = re.search(inwardCode, postcode)
    if matches is None:
        response["errors"].append("inward code Invalid")
    return postcode


def validatePostCode(postcode):
    response = buildResponse()
    validateLength(postcode, response)
    validateOutwardCode(postcode, response)
    validateInwardCode(postcode,response)

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
