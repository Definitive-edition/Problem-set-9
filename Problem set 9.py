#Aditya Chunduru
#00335780
#Problem Set 9
#CIS 153 L8
#Program description: Tkinter GUI app.



import tkinter as tk 
#Exercise 1
#function call for dislpaying message
def display_hello():
    label.config(text="Hello")

#Main window creation
root = tk.Tk()
root.title("Hello GUI")



#Make a Label
label = tk.Label(root, text="Click the button to display 'Hello'")
label.pack(pady=10)



#Create a button 

button = tk.Button(root, text="click me", command=display_hello)









#Exercise 2 

def calculate_sum():
    try: 
        #Get values from textboxes and calculate sum
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2


        result_label.config(text=f"Sum: {result}")
    except ValueError: 

        result_label.config(text="Invalid input. Please enter numbers.")


#title of web service
root = tk.Tk()
root.title("Sum Calculator")

#user prompt within GUI
label1 = tk.Label(root, text="Enter number 1:")
label1.pack()


entry1 = tk.Entry(root)
entry1.pack()
#user prompt in GUI
label2 = tk.Label(root, text="Enter number 2:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()
#Button for calcuating sum.
calculate_button = tk.Button(root, text="calculate sum", command=calculate_sum)
calculate_button.pack()

result_label = tk.Label(root, text="Sum:")
result_label.pack()

#Running the GUI
root.mainloop()