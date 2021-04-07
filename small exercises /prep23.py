import string

def every_other(text):
    text_split = text.split()
    index = 0
    result = ""
    while index < len(text_split):
        result +=  text_split[index] + " "
        index += 2
    return result.lstrip()
