import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch data from the Flask server
def fetch_data():
    try:
        student_id = int(entry_id.get())
        response = requests.get(f'http://localhost:5000/getstudent/{student_id}')
        
        if response.status_code == 200:
            data = response.json()
            result_text.set(f"ID: {data['id']}\nName: {data['name']}\nAge: {data['age']}\nEmail: {data['email']}\nGrade: {data['grade']}")
        else:
            result_text.set("Student not found")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid ID.")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Student Data Fetcher")

# Create and place widgets
tk.Label(root, text="Enter Student ID:").pack(pady=20)
entry_id = tk.Entry(root)
entry_id.pack(pady=10)

tk.Button(root, text="Fetch Data", command=fetch_data).pack(pady=20)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text).pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
