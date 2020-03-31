import ModRing
from ModRing import IntegerModRing
import re

alphabet = "\n abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,;:!?.'()&%-+*/"
p = 10


def encodageBloc(message):
    """returns the integer which codes the message """
    n = 0
    cpt = 0
    for _ in message:
        n += alphabet.index(_)*(len(alphabet)**cpt)
        cpt += 1
        # tab.append(alphabet.index(_))
    return n

def decodageBloc(n):
    """returns the message coded by the number n"""
    message=""
    cpt = p-1
    while cpt != -1:
        letter = alphabet[n//((len(alphabet)**cpt))]
        n = n%((len(alphabet)**cpt))
        cpt -= 1
        message = letter+message
    return message


def encode(message):
    """parses the message into 10 chars blocs"""
    parsedMessage = re.findall('.{1,10}', message)
    integerList = []
    for _ in parsedMessage:
        integerList.append(encodageBloc(_))
    return integerList

def decode(integerList):
    """converts the integerList into the final message"""
    message = ""
    for _ in integerList:
        message = message+decodageBloc(_)
    return message