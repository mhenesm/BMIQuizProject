from tkinter import *

# Window
window = Tk()
window.title("BMI CALCULATOR")
window.minsize(width=150, height=300)
window.config(padx=75, pady=100)

# Label1
label1 = Label(text="Enter Your Weight (kg)")
label1.pack()

# Entry1
entry1 = Entry(width=20)
entry1.pack()

# Label2
label2 = Label(text="Enter Your Height (cm)")
label2.pack()

# Entry2
entry2 = Entry(width=20)
entry2.pack()

# Label2
label= Label(text="BMI")
label.pack()


# Button function
def button_clikced():
    try:
        t1 = int(entry1.get())
        t2 = int(entry2.get())
        BMI = round((t1 / (t2 ** 2) )*10000 , 1)
        if BMI < 18.5 :
            label.config(text=str(BMI) + " : UNDERWEIGHT")
        elif 18.5<= BMI <= 24.9 :
            label.config(text=str(BMI)+ " : NORMAL")
        elif 25 <= BMI <= 29.9 :
            label.config(text=str(BMI) + " : OVERWEIGHT")
        elif 30 <= BMI <= 34.9 :
            label.config(text=str(BMI) + " : OBESE")
        elif 35< BMI :
            label.config(text=str(BMI) + " : EXTREMLY OBESE")
    except ValueError:
        label.config(text="Incorrect entry please enter a valid integer!")

# Button
button = Button(text="Calculate", command=button_clikced)
button.config(padx=10, pady=10)
button.pack()

window.mainloop()
