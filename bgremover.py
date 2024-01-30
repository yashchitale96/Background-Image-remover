import tkinter as tk
from rembg import remove
from PIL import Image
from tkinter import filedialog, messagebox
import os

def upload_file():
    global filename
    f_types = [('Jpg Files', '*.jpg'),('allfiles','*')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if len(filename) > 0:
        b1.config(state='disabled')

def select_output_directory():
    global output_directory
    output_directory = filedialog.askdirectory()
    if len(output_directory) > 0:
        output_label.config(text=f"Output Directory: {output_directory}")
        output_label.grid(row = 3, column=2, padx=20)

def clear_default_text(event):
    if image_name.get() == 'Enter file name':
        image_name.set('')

def convert(image_name):
    if not filename:
        messagebox.showwarning('Warning', 'Please select an image first.')
        return
    
    if not output_directory:
        messagebox.showwarning('Warning', 'Please select an output directory.')
        return

    try:
        current_working_directory = os.getcwd()
        input_path = filename
        output_path = os.path.join(output_directory, f'{image_name}.png')

        image_input = Image.open(input_path)
        output = remove(image_input)
        output.save(output_path)
        messagebox.showinfo('Success', 'Image background successfully removed')
        top.destroy()
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {str(e)}')

top = tk.Tk()
top.geometry("750x400")
top.title('Celebrare')

filename = ''
output_directory = ''

my_font1 = ('times', 18, 'bold')

l1 = tk.Label(top, text='Background Removal App', width=50, font=my_font1)
l1.grid(row=1, column=2, pady=10)

b1 = tk.Button(top, text='Select Image', height=2, font=('Arial', 13,'bold'), bg='#dc3545', fg='white', command=upload_file)
b1.grid(row=2, column=2, pady=10)

output_label = tk.Label(top, text='Output Directory: Not selected', font=('Arial', 12))
output_label.grid(row=3, column=2, pady=5)

b2 = tk.Button(top, text='Select Output Directory', height=2, font=('Arial', 12, 'bold'), bg='#007bff', fg='white', command=select_output_directory)
b2.grid(row=4, column=2, pady=10)

image_name = tk.StringVar(top)
image_name.set('Enter file name')

e1 = tk.Entry(top, textvariable=image_name, font=('Arial',12), justify='center')
e1.grid(row=5, column=2, pady=15)
e1.bind("<FocusIn>", clear_default_text)

b3 = tk.Button(top, text='Convert now', height=2, font=('Arial', 13, 'bold'), bg='#dc3545', fg='white', command=lambda: convert(image_name.get()))
b3.grid(row=6, column=2, pady=10)

top.mainloop()
