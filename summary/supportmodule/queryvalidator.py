import validators
def isURL(url):
    valid=validators.url(url)
    return valid==True
        