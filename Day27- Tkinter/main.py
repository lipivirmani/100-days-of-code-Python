from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=100)
window.config(padx=20,pady=20)
#Label


def miles_to_km():
    mile= float(miles_input.get())
    result = round(mile * 1.609)
    km_result.config(text=f"{result}")


miles_label = Label(text= "Miles", font=("Arial", 18))
miles_label.grid(column= 2,row= 0) # Makes the label to show
# miles_label.config(pady=10,padx=10)

is_equal= Label(text="is equal to", font=("Arial", 18))
is_equal.grid(column= 0 , row= 2)

km_result = Label(text="0")
km_result.grid(column= 1, row = 2)

km_label = Label(text="Km", font=("Arial", 18))
km_label.grid(column= 2, row= 2)

button = Button(text="Convert", command=miles_to_km)
button.grid(column= 1,row= 6)


miles_input = Entry(width=8)
miles_input.grid(column= 1, row=0)

# window remains open
window.mainloop()
