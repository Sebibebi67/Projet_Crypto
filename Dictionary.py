import ModRing
from ModRing import IntegerModRing
import re
import random

alphabet = "\n abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,;:!?.'()&%-+*/"
charList = list(alphabet)
random.shuffle(charList)
alphabet = "ø"+"".join(charList)

p = 12


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
    """Parses the message into p chars blocs"""
    string = '.{1,'+str(p)+'}'
    parsedMessage = re.findall(string, message)
    integerList = []
    for block in parsedMessage:
        integerList.append(encodingBlock(block))
    return integerList

def decoding(integerList):
    """Converts the integerList into the final message"""
    message = ""
    for integer in integerList:
        message = message+decodingBlock(integer)
    return message

def example():
    print("------Testing Dictonary------")
    print("\n\n")

    print("------This is our alphabet------")
    print(alphabet)
    print("\n\n")


    print("------This is the length of each block------")
    print("block length value : ", p)
    print("\n\n")

    print("------This is our message we want to code------")
    message = "Cryptography is a method of protecting information and communications through the use of codes so that only those for whom the information is intended can read and process it. The pre-fix 'crypt' means 'hidden' or 'vault' and the suffix 'graphy' stands for 'writing'. In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms to transform messages in ways that are hard to decipher. These deterministic algorithms are used for cryptographic key generation and digital signing and verification to protect data privacy, web browsing on the internet and confidential communications such as credit card transactions and email."
    print("message : ", message)
    print("\n\n")

    print("------Let's encode our message------")
    codedMessage = encoding(message)
    print("encoded message : ", codedMessage)
    print("\n\n")

    print("------Now we can try to decode this message------")
    decodedMessage = decoding(codedMessage)
    print("decoded message : ", decodedMessage)
    print("\n\n")