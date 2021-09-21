import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

print ("Identify is Phrase Palindrome Or not\n")
phrase = input("Enter phrase: ")
result = is_palindrome(phrase)
print (result)
