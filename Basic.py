import json
data=json.load(open("data.json"))
def translate(w):
    if w in data:
        return w
    else:
        return "The Word doesn't exists please double check it."

word=input("Say Somethings")
print(translate(word))