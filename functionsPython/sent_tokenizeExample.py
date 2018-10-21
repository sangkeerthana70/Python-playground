from nltk.tokenize import sent_tokenize

def main():
    stringA = "Whenever I smell strong tobacco smoke when I'm in an enclosed space such as a room, train, or aircraft, I begin to get angry. There are several reasons. First, medical researchers have shown that secondhand smoke, that is, the smoke from other people's cigarettes, causes cancer and other health problems. If the smoke were car exhaust or burning trash, we would put out the fire and open the windows to get rid of the smoke."
    stringB = "Whenever I smell tobacco smoke when I'm in an enclosed space such as a room, train, or aircraft, I get angry. There are more reasons. First, medical researchers have shown that secondhand smoke, that is, the smoke from other people's cigarettes, causes cancer and other health problems. If the smoke was car exhaust or burning trash, we put out the fire and open the windows to get rid of smoke."
    listA = sent_tokenize(stringA)
    listB = sent_tokenize(stringB)
    print(listA)
    print(listB)
    print(similarSentences(listA, listB))
    return(similarSentences(listA, listB))


def similarSentences(listA, listB):
    return list(set(listA) & set(listB))

if __name__ == '__main__':
    main()