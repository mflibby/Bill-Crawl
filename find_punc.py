def recursive_punc_find(full_doc, row_index, char_index, sentence, direction, recurslevel):
    for i in full_doc[row_index][::direction][char_index:]:
        sentence.append(i)

        if i == '.':
            #print(i)
            return sentence[::direction]
    #print(sentence)
    if recurslevel < 2:
        return recursive_punc_find(full_doc, row_index+direction, 0, sentence, direction,recurslevel+1)
    else:
        return sentence[::direction]
