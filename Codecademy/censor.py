def censor(text, word):
    arr = text.split(" ")
    for ind, w in enumerate(arr):
        if w == word:
            arr[ind] = "*" * len(w)
    return " ".join(arr)

text = input("Enter text: ")
word = input("Enter censored word: ")
print (censor(text,word))
