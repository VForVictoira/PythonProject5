from tkinter import *

pw = PanedWindow(orient=VERTICAL)
pw.pack(fill=BOTH, expand=True)

top = Label(pw,text='Top Pane')
pw.add(top)

bottom = Label(pw,text='Bottom Pane')
pw.add(bottom)

pw.mainloop()