import ModRing
from ModRing import IntegerModRing
import re
import random

alphabet = "\n abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,;:!?.'()&%-+*/"
charList = list(alphabet)
random.shuffle(charList)
alphabet = "ø"+"".join(charList)

p = 13


def encodingBlock(message):
    """returns the integer which codes the message """
    n = 0
    cpt = 0
    for char in message:
        n += alphabet.index(char)*(len(alphabet)**cpt)
        cpt += 1
    return n

def decodingBlock(n):
    """returns the message coded by the number n"""
    message=""
    cpt = p-1
    while cpt != -1:
        letter = alphabet[n//((len(alphabet)**cpt))]
        n = n%((len(alphabet)**cpt))
        cpt -= 1
        if letter != "ø":
            message = letter+message
    return message


def encoding(message):
    """Parses the message into 10 chars blocs"""
    string = '.{1,'+str(p)+'}'
    parsedMessage = re.findall(string, message)
    integerList = []
    for block in parsedMessage:
        integerList.append(encodingBlock(block))
    return integerList

def decoding(integerList):
    """converts the integerList into the final message"""
    message = ""
    for integer in integerList:
        message = message+decodingBlock(integer)
    return message