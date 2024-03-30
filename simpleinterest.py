from tkinter import *
window = Tk()
window.title("BMI Calculator")
window.geometry("380x400")
window.configure(bg="lightyellow")

def calculate_si():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(1, 2)
    showlabel.destroy()
    message = Label(result_frame, text=f"Interest on Rs."+str(p)+" at the rate of "+str(r)+" for "+str(t)+" years is Rs."+str(interest), bg="lightyellow", font=("Calibri",12), width=55)
    message.place(x=20, y=40)
    message.pack()        



app_label = Label(window, text="Simple Interest Calculator", fg="black", bg="lightyellow", font=("Calibri",20), bd=5)
app_label.place(x = 50 , y = 20)

principle_label = Label(window, text="Enter Principle", fg="black", bg="lightyellow", font=("Calibri",12), bd=5)
principle_label.place(x = 20 , y = 90)

principle = Entry(window, text="", bd=2, width=22)
principle.place(x = 150 , y = 92)

rate_label = Label(window, text="Enter Rate", fg="black", bg="lightyellow", font=("Calibri",12), bd=5)
rate_label.place(x = 20 , y = 140)

rate = Entry(window, text="", bd=2, width=22)
rate.place(x = 150 , y = 142)

time_label = Label(window, text="Enter Time", fg="black", bg="lightyellow", font=("Calibri",12), bd=5)
time_label.place(x = 20 , y = 185)

time = Entry(window, text="", bd=2, width=22)
time.place(x = 150 , y = 187)

calculate_button = Button(window, text="Calculate", fg="black", bg="yellow", font=("Calibri",12), bd=5, command=calculate_si)
calculate_button.place(x = 20 , y = 250)

result_frame = LabelFrame(window, text="Result", fg="black", bg="lightyellow", font=("Calibri",12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x = 20 , y = 300)

showlabel = Label(result_frame, text="", fg="black", bg="lightyellow", font=("Calibri",12), width=55)
showlabel.place(x = 20 , y = 20)
showlabel.pack()

window.mainloop()