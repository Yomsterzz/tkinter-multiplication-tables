import tkinter as tk

def generate_tables():
    num = int(number_entry.get())
    for i in range(range_var.get()+1):
        answer = num*i
        result_text.insert(tk.END, "{} x {} = {}\n".format(num, i, answer))
        

window = tk.Tk()
window.title("Mathematical Table Generator")
window.geometry("600x600")
window.configure(bg="#e0f2b7")

title_label = tk.Label(window, text="Mathematical Table Generator", font=("Arial", 26, "bold"), bg="#e0f2b7")
title_label.pack(pady=10)

frame = tk.Frame(window, bg="#e0f2b7")
frame.pack(pady=10)

number_label = tk.Label(frame, text="Enter a Number:", font=("Arial", 22), bg="#e0f2b7")
number_label.pack(side=tk.LEFT, padx=5)

number_entry = tk.Entry(frame, width=10, font=("Arial", 22))
number_entry.pack(side=tk.LEFT, padx=5)

range_frame = tk.Frame(window, bg="#e0f2b7")
range_frame.pack(pady=10)

range_label = tk.Label(range_frame, text="Select Range:", font=("Arial", 22), bg="#e0f2b7")
range_label.pack(side=tk.LEFT, padx=5)

range_var = tk.IntVar(value=10)

range10 = tk.Radiobutton(range_frame, text="10", variable=range_var, value=10, bg="#e0f2b7")
range10.pack(side=tk.LEFT, padx=5)

range20 = tk.Radiobutton(range_frame, text="20", variable=range_var, value=20, bg="#e0f2b7")
range20.pack(side=tk.LEFT, padx=5)

range30 = tk.Radiobutton(range_frame, text="30", variable=range_var, value=30, bg="#e0f2b7")
range30.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(window, text="Generate Table", font=("Arial", 22), command=generate_tables)
generate_button.pack(pady=10)

result_text = tk.Text(window, width=30, height=15, font=("Courier", 15), bg="white", fg="black")
result_text.pack(pady=10)

window.mainloop()