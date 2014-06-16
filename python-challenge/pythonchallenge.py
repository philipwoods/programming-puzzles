# File: pythonchallenge.py

from string import maketrans
import re
import urllib
import cPickle
import zipfile


#
# Level 0
#
# Change the 0.html to 274877906944.html

#
# Level 1
#
def caesar(mesg, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    outMesg = ""
    for letter in mesg:
        if letter.isalpha():
            position = alphabet.find(letter)
            outMesg += alphabet[(position + shift)%26]
        else:
            outMesg += letter
    return outMesg

# apparently this is built in as string.maketrans()
def betterCaesar(mesg, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shiftedAlpha = ""
    for i in range(len(alphabet)):
        shiftedAlpha += alphabet[(i+shift)%26]
    transTable = maketrans(alphabet, shiftedAlpha)
    return mesg.translate(transTable)
# Change the map.html to ocr.html

#
# Level 2
#
def findChars(mesg, threshhold):
    result = ""
    commonChars = {}
    for char in mesg:
        if (char not in commonChars) and (mesg.count(char) <= threshhold):
            result += char
        else:
            commonChars[char] = 1
    return result
# Change the ocr.html to equality.html

#
# Level 3
#
def level3(text):
    pattern = '(?<=[a-z][A-Z]{3})[a-z](?=[A-Z]{3}[a-z])'
    result = re.findall(pattern, text)
    return result
# Change the equality.html to linkedlist.php

#
# Level 4
#
def redirect(nothing=12345):
    pattern = '(?<=and the next nothing is )[0-9]+'
    urlBase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    nothings = []
    url = ""
    page = urllib.urlopen(urlBase + str(nothing))
    lines = page.readlines()
    for line in lines:
        match = re.search(pattern, line)
        if match:
            nothing = match.group()
            nothings.append(nothing)
            break
    page.close()
    for i in range(400):
        url = urlBase + str(nothing)
        page = urllib.urlopen(url)
        lines = page.readlines()
        for line in lines:
            match = re.search(pattern, line)
            if match:
                nothing = match.group()
                nothings.append(nothing)
                break
        page.close()
    return nothings
# Change the url to http://www.pythonchallenge.com/pc/def/peak.html

#
# Level 5
#
def peakhell():
    banner = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
    obj = cPickle.Unpickler(banner).load()
    out = ""
    for line in obj:
        for tup in line:
            out += tup[0]*tup[1]
        out += "\n"
    print out
# Change peak.html to channel.html

#
# Level 6
#
def zipped():
    archive = zipfile.ZipFile("C:\Users\Philip\Downloads\channel.zip", 'r')
    comments = []
    answer = ''
    nothing = '90052'
    nextNothing = ziphelp(nothing, archive, comments)
    while nextNothing:
        nothing = nextNothing
        nextNothing = ziphelp(nothing, archive, comments)
    archive.close()
    print nothing
    for letter in comments:
        if letter.isalpha() and (letter not in answer):
            answer += letter
    return answer

def ziphelp(number, filename, storage):
    pattern = '(?<=Next nothing is )[0-9]+'
    txt = filename.open(number + '.txt')
    contents = txt.readline()
    match = re.search(pattern, contents)
    storage.append(filename.getinfo(number + '.txt').comment)
    if match:
        return match.group()
    else:
        return
# Change channel.html to oxygen.html
