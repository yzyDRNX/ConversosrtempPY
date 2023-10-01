import tkinter as tk 

def reset():
    entry1.delete(0, tk.END)
    entry1.insert(0,"0.0")
    entry2.delete(0, tk.END)
    entry2.insert(1,"0.0")
def convert_to_celsius():
    fahrenheit = float(entry1.get())
    celcius = (fahrenheit - 32) * 5.0 / 9.0
    entry2.delete(0, tk.END)
    entry2.insert(0, f"{celcius:.2f}")
def convert_to_fahrenheit():
    celcius = float(entry2.get())
    fahrenheit = (celcius * 9 / 5) + 32
    entry1.delete(0, tk.END)
    entry1.insert(0, f"{fahrenheit:.2f}")

app = tk.Tk()
app.title("Conversor de Temperatura")

label1 = tk.Label (app, text="Fahrenheit: ")
label1.grid(row=0, column=0)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)
button1 = tk.Button(app, text="Convertir a Celsius" ,command=convert_to_celsius) 
button1.grid(row=0, column=2)

label2 = tk.Label(app, text="Celsius: ") 
label2.grid(row=1, column=0)

entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

button2 = tk.Button(app, text="Convertir a Fahrenheit", command=convert_to_fahrenheit)
button2.grid(row=1, column=2)

button3 = tk.Button(app, text="Restablecer", command=reset)
button3.grid(row=2, column=1)

app.mainloop()

