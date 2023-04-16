from tkinter import*
window=Tk()
window.title("Hello Renoir!")
window.geometry("400x400")

photo = PhotoImage(file="C:\Users\Oh Seung Hun\Desktop\gif\dog.gif")
label1=Label(window,image=photo)

label1.pack()

window.mainloop()