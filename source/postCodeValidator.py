def validatePostCode(postcode):
    response = buildResponse()
    return response


def buildResponse():
    response = {
        "postCode": "",
        "errorCode": 0,
        "errors": []
    }
    return response
