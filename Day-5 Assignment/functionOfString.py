user_string = "India123"
if user_string.isalnum():
    print(user_string, ': The String is alphanumeric.')

user_string = "1974"
if user_string.isdigit():
    print(user_string, ': The String contains only digits.')

user_string = "India"
if user_string.isalpha():
    print(user_string, ': String contains only alphabetic characters.')

user_string = "   "
if user_string.isspace():
    print(user_string, ': String contains only whitespace characters.')

user_string = "INDIA"
if user_string.isupper():
    print(user_string, ': All letters in the string are uppercase.')

user_string = "india 1974"
if user_string.islower():
    print(user_string, ': All letters in the string are lowercase.')

user_string = "India 1974"
toLower = user_string.lower()
print(user_string, ': Convert String in lowercase:', toLower)

toUpper = user_string.upper()
print(user_string, ': Convert String in uppercase:', toUpper)

# lstrip() Returns a copy of the string with all leading whitespace
# characters removed, that appear at the beginning of the string.
user_string = "   India 1974"
print('Left Strip:', user_string.lstrip())

user_string = "India 1974"
print('Left Strip with Character A:', user_string.lstrip('I'))

user_string = "India 1974     "
print('Right Strip:', user_string.rstrip('A'))

user_string = "India"
print('Right Strip with Character a:', user_string.rstrip('a'))

user_string = "   India 1974    "
print('Strip from both side :', user_string.strip())

user_string = "India America Russia Japan China"
print('Strip with Character A:', user_string.strip('I'))
print('Strip with Character a:', user_string.strip('a'))

print('\nStartswith check if a string starts with a specified substring')
user_string = "India"
print(user_string.startswith('Ind'))
print(user_string.startswith('Rolum'))

print('\nEndswith check whether a string ends with a specified substring')
user_string = "India"
print(user_string.endswith('dia'))
print(user_string.endswith('mia'))

user_string = "Columbia"
print(user_string.find('lumbia'))
print(user_string.find('colbia'))
print(user_string.find('bia'))
print(user_string.find('col'))
print(user_string.find('Col'))

user_string = "Hello India"
old = "India"
new = "Russia"
print(user_string.replace(old, new))