import tkinter as tk

def click_one():
    return(True)
def click_two():
    return(False)

window=tk.Tk()
window.title("Bank application")

frame= tk.Frame(master=window)
btn_Button1=tk.Button(master=frame, text=("withdraw"), command=click_one())
btn_Button2=tk.Button(master=frame, text=("deposit"),command=click_two())

frame.grid(row=0, column=0)
btn_Button1.grid(row=0, column=0)
btn_Button2.grid(row=2, column=0)


window.mainloop()