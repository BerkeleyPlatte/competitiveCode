# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in
# the input string. The input string can be assumed to contain only
# alphabets (both uppercase and lowercase) and numeric digits.


def duplicate_count(text):
    all_lowered = []
    for each in text:
        if each.isalpha():
            all_lowered.append(each.lower())
        else:
            all_lowered.append(each)
    the_dict = {}

    for each in all_lowered:
        the_dict[each] = []
    for each in all_lowered:
        for key, value in the_dict.items():
            if key == each:
                value.append(each)
    count = 0
    for each in the_dict.values():
        if len(each) > 1:
            count += 1
    return count