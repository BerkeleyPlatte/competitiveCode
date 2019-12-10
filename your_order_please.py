# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.


def order(sentence):
    solution = []
    sol_str = ' '
    sentence_list = sentence.split(' ')
    nums_dict = dict.fromkeys(range(1, 10), [])
    for each_word in sentence_list:
        for key in nums_dict:
            if str(key) in each_word:
                nums_dict[key] = each_word
    for key in nums_dict:
        if len(nums_dict[key]) > 0:
            solution.append(nums_dict[key])
    return sol_str.join(solution)


print(order("is2 Thi1s T4est 3a"))
