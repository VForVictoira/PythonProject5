from tkinter import *

window = Tk()
window.title("Marks")
window.resizable(False, False)

text = Text(window, width=30, height=20)

for i in range(1,10):
    text.insert(END, str(i)+'TestTESTETSTESTETSTE\n')

#设置书签
text.mark_set('mark1','1.0')
text.mark_set('mark2','5.0')
print(text.get('mark1','mark2'))

text.pack(fill=BOTH, expand=True)

window.mainloop()

