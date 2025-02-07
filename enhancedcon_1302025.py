import tkinter as tkk

skibidi = tkk.Tk()
skibidi.title('Enhanced convarter')
skibidi.geometry('300x300')

a = tkk.StringVar()
e1 = tkk.Entry(skibidi, textvar=a)
e1.place(x=50, y=50)

fa = tkk.Label(skibidi, text='Celsius')
fa.place(x=200, y=50)

b = tkk.StringVar()
e2 = tkk.Entry(skibidi, textvar=b)
e2.place(x=50, y=200)

fb = tkk.Label(skibidi, text='Farenheit')
fb.place(x=200, y=200)

c = tkk.StringVar(value='C to F')
options = ['C to F', 'F to C']

def labelchange(*arg):
    if c.get()=='C to F':
        fa.config(text='Celsius')
        fb.config(text='Farenheit')
    else:
        fa.config(text='Fahrenheit')
        fb.config(text='Celsius')
        
op1 = tkk.OptionMenu(skibidi, c, *options, command=labelchange)
op1.place(x=100, y=100)

def convert():
    try:
        value = float(a.get())
        if c.get()=='C to F':
            ans = (value*1.8)+32
            b.set(f'{ans:.2f}')

        elif c.get()=='F to C':
            ans = (value-32)/1.8
            b.set(f'{ans:.2f}')
    except:
        b.set('Invalid input..:(')

b1 = tkk.Button(skibidi, text='ConVERT now', command=convert)
b1.place(x=50, y=150)


skibidi.mainloop()
