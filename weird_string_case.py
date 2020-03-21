#Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd 
#indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

#The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a 
#single space(' ').


def to_weird_case(string):
    string_list = list(string)
    altered_list = []
    for index, value in enumerate(string_list):
        if value.isalpha():
            if index % 2 == 0:
                altered_list.append(value.upper())
            else:
                altered_list.append(value.lower())
        else:
            altered_list.append(value)
    return ''.join(altered_list)

print(to_weird_case('This')) 