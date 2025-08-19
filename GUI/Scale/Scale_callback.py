from tkinter import *

def bgUpdate(source):
    red = rSlider.get()
    green =gSlider.get()
    blue = bSlider.get()
    print("R=%d, G=%d, B=%d" % (red, green, blue))
    myColor="#%02x%02x%02x" % (int(red), int(green), int(blue))
    window.config(bg=myColor)


window = Tk()
window.title("Scale_callback")
window.geometry("300x300")
Slider = LabelFrame(window,text='Adjust Color')
Slider.pack(anchor=E, padx=5, pady=5)
rSlider = Scale(Slider, from_=0, to=255, command=bgUpdate)
gSlider = Scale(Slider, from_=0, to=255, command=bgUpdate)
bSlider = Scale(Slider, from_=0, to=255, command=bgUpdate)
gSlider.set(125)
rSlider.grid(row=0, column=0)
bSlider.grid(row=0, column=1)
gSlider.grid(row=0, column=2)
window.mainloop()