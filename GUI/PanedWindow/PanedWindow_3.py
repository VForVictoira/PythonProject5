from tkinter import *


pw = PanedWindow(orient=HORIZONTAL)
pw.pack(fill=BOTH, expand=1,padx=5,pady=5)

entry = Entry(pw,bd=3)
pw.add(entry)

pwin = PanedWindow(pw,orient=VERTICAL)
pw.add(pwin)

scale = Scale(pwin,orient=HORIZONTAL)
scale2 = Scale(pwin,orient=HORIZONTAL)

pwin.add(scale)
pwin.add(scale2)
pw.mainloop()