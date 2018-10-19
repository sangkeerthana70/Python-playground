from nltk.tokenize import sent_tokenize

a = "The New England Patriots are a professional American football team based in the Greater Boston region.\n The Patriots compete in the National Football League as a member club of the league's American Football Conference \nEast division\n I am a Patriots fan"
b = "The Patriots compete in the National Football League as a member club of the league's American Football Conference \nEast division\n I am a Patriots fan"
listA = a.splitlines()
listB = b.splitlines()
print(listA)
print(listB)

def  intersection(listA, listB):
    return list(set(listA) & set(listB))
print(intersection(listA, listB))


