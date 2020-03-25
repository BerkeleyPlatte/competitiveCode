def top_3_words(text):
    if any(each.isalpha() for each in text):
        letters = "abcdefghijklmnopqrstuvwxyz "
        no_punc = []
        for each in text.lower():
            if each in letters:
                no_punc.append(each)
            elif each == "'":
                index = text.index(each)
                if text[index - 1] in letters or text[index + 1]:
                    no_punc.append(each)
        word_list = [each for each in "".join(no_punc).split()]
        pairs = []
        for each in word_list:
            count = 0
            for i in range(len(word_list)):
                if each == word_list[i]:
                    count += 1        
            if [each, count] not in pairs:
                pairs.append([each, count])
        nums = []
        for each in pairs:
            for each in str(each[1]):
                if each not in nums:
                    nums.append(each)
        real_nums = [int(each) for each in nums]
        real_nums.sort()
        real_nums.reverse()
        if len(real_nums) > 3:
            final_three = real_nums[:3]
        else:
            final_three = real_nums
        final_three_str = [str(each) for each in final_three]
        answer = []
        while len(answer) <= 3:
            for each_final in final_three_str:
                for each_pair in pairs:
                    if each_final == str(each_pair[1]):
                        answer.append(each_pair[0])
            return answer
    else:
        return []
                
                

print(top_3_words("  //wont won't won't "))