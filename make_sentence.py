from find_punc import *

def obtain_sentence(full_doc,readline, row_index, char_index):
    line_array = [i for i in readline]

    dollar_amount_list = []
    dollar_amount = ''
    sentence_list = []
    sentence = ''
    sentence_list2 = []
    sentence2 = ''
    for i in line_array[char_index:]:
        if i.isalpha():
            break
        dollar_amount_list.append(i)
    for i in dollar_amount_list[:-1]:
        dollar_amount+=i

    sentence_list = recursive_punc_find(full_doc, row_index, char_index, sentence_list, 1,0)
    #print('done1')
    sentence_list2 = recursive_punc_find(full_doc,row_index,len(line_array)-char_index,sentence_list2,-1,0)
    #print(sentence_list2)



    for i in sentence_list2:
        sentence += i
        #print(i)
    for i in sentence_list:
        sentence += i
    return dollar_amount, sentence
