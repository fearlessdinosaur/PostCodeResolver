# Validations based on https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
# as of 17/06/22
import re

outwardCodeRegex = '^[A-Z]{1,2}[0-9][A-Z0-9]? '
inwardCodeRegex = '[0-9][A-Z]{2}$'
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
    matches = re.search(outwardCodeRegex, postcode)
    if matches is None:
        response["errors"].append("outward code Invalid")
    return postcode


def validateInwardCode(postcode, response):
    matches = re.search(inwardCodeRegex, postcode)
    if matches is None:
        response["errors"].append("inward code Invalid")
    return postcode


def validatePostCode(postcode):
    response = buildResponse()
    validateLength(postcode, response)
    validateOutwardCode(postcode, response)
    validateInwardCode(postcode, response)

    if len(response["errors"]) > 0:
        response["errorCode"] = 1
    return response


def getParts(postcode):
    # using the outward code regex with the space stripped to match unformatted strings
    outward_code = re.search(outwardCodeRegex[:-1], postcode)
    inward_code = re.search(inwardCodeRegex, postcode)

    codes = {
        "outwardCode": outward_code.group(0) if outward_code is not None else "",
        "inwardCode": inward_code.group(0) if inward_code is not None else ""
    }
    return codes


def formatPostCode(postcode):
    response = buildResponse()
    validateLength(postcode, response)

    if len(response["errors"]) == 0:
        parts = getParts(postcode)

        if parts["outwardCode"] != "" and parts["inwardCode"] != "":
            response["postCode"] = "{0} {1}".format(parts["outwardCode"], parts["inwardCode"])
        else:
            response["errorCode"] = 1
            response["errors"].append("given postcode cannot be formatted")
    else:
        response["errorCode"] = 1
    return response


def buildResponse():
    response = {
        "postCode": "",
        "errorCode": 0,
        "errors": []
    }
    return response
