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

text.tag_add('tag1','mark1','mark2')
text.tag_config('tag1',foreground='blue',background='red')
text.pack(fill=BOTH, expand=1)
window.mainloop()