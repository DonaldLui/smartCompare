from tkinter import *
from difflib import SequenceMatcher

window = Tk()
window.title('Smart Compare')
window.resizable(width=False, height=True)

def analyzefiles():
    w1 = wordEntry1.get()
    w2 = wordEntry2.get()
    if w1 != "" and w2 != "":
        ratio = SequenceMatcher(None, w1, w2).ratio()
        print(ratio)
    else:
        ratio = "Enter words to compare!"
        print(ratio)


wordEntry1 = Entry(window)
wordEntry2 = Entry(window)
runButton = Button(window, text="Run", bg="blue", fg="white", command=analyzefiles)

wordEntry1.grid(row="0")
wordEntry2.grid(row="1")
runButton.grid(row="2")

window.mainloop()


