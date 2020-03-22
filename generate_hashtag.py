# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    capd_list = [each for each in s.title().strip()]
    for each in capd_list:
        if each == ' ':
            capd_list.remove(each)
    final = '#' + ''.join(capd_list).strip()
    new_final = ''.join(final.split())
    if len(new_final) > 140 or s == '':
        return False
    else:
        return new_final


print(generate_hashtag('Codewars      '))