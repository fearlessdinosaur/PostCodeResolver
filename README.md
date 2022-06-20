# Post Code Resolver
Author: David Fox

Date: 20/06/2022

## How to use
the post code resolver has two main functions that are callable by creating an instance
of the PostCodeResolver.

### validatePostCode(postcode): 
this function takes in a string postcode and returns the standard response payload
below containing a list of any errors which occur. The errors are as follows:
- `outward code invalid` : The given outward code was found not to match the expected format
- `inward code invalid` : The given inward code was found not to match the expected format
- `given postcode is too long` : The given postcode was more than 8 characters in length
- `given postcode is too short` : The given postcode was less than 6 characters in length

any errors will result in an error code of 1, while a valid postcode will recieve
an error code of 0.

### formatPostCode(postcode):
this function takes in a string postcode and returns the standard response payload
below which will contain either the newly formatted postcode and an errorcode of 0,
or a list of errors and an error code of 1. The errors are as follows:
- `given postcode is too long` : The given postcode was more than 8 characters in length
- `given postcode is too short` : The given postcode was less than 6 characters in length
- `given postcode cannot be formatted` : The given postcode cannot be split into a outward code and an inward code and formatted

## Resolver Payload
The resolver uses a standardised payload which looks like:

```
{ 
    name: string
    errorCode: 1|0
    errors: []
}
```