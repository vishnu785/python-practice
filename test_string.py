arn = "arn:aws:iam::123456789012:user/JohnDoe"
# string-in built function
print(arn.split("/")[1])
#output= find specific list in between string(FROM JSON FILE)

#string split
text = "Python is awesome"
words = text.split()
print("Words:", words)
#output= specify words betn string(text)

# string data type in built function
name = "vishnu"
print(name.upper())
#output= Capital letter

# String Concatenation = String concatenation means add strings together,
# Use the + character to add a variable to another variable:
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2 
print(result)
#output= adding two string together

# It returns an integer which is the length of the string
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)
#output= numbers of characters in between string

#Upper&Lowercase
text = "we are learning python for devops"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:",lowercase)
#output= capital and small letter

# string replace
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)
#output= replace specific character

#sting strip
text = "   some spaces around    "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
#output= remove spaces(only begin and end)
# &&
import re

text = "   Some    spaces   around   "
stripped_text = re.sub(' +', ' ', text.strip())
print("Stripped text:", stripped_text)
#output= all space removed

#string and substring
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
#output= find specific character


    

