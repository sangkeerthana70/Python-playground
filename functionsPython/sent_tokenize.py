from nltk.tokenize import sent_tokenize

stringInput = "Unicode is a character encoding standard that has widespread acceptance. Microsoft software uses Unicode at its core. Whether you realize it or not, you are using Unicode already!"

tokenizedString = sent_tokenize(stringInput)
print(tokenizedString)