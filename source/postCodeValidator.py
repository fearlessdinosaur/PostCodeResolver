def validateLength(postcode, response):
    codeLength = len(postcode)
    minlength = 6
    maxlength = 8
    if codeLength > maxlength or codeLength < minlength:
        if (codeLength > maxlength):
            response["errors"].append("given postcode is too long")
        if (codeLength < minlength):
            response["errors"].append("given postcode is too Short")


def validatePostCode(postcode):
    response = buildResponse()
    validateLength(postcode, response)

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
