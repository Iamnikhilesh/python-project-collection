import tkinter as tk
from tkinter import messagebox

# Function to handle length conversion
def length_conversion():
    value = float(entry.get())
    if selected_unit.get() == "Meters to Kilometers":
        result = value / 1000
    elif selected_unit.get() == "Kilometers to Meters":
        result = value * 1000
    elif selected_unit.get() == "Meters to Centimeters":
        result = value * 100
    elif selected_unit.get() == "Centimeters to Meters":
        result = value / 100
    result_label.config(text=f"Result: {result:.2f}")

# Function to handle weight conversion
def weight_conversion():
    value = float(entry.get())
    if selected_unit.get() == "Kilograms to Grams":
        result = value * 1000
    elif selected_unit.get() == "Grams to Kilograms":
        result = value / 1000
    result_label.config(text=f"Result: {result:.2f}")

# Function to handle temperature conversion
def temperature_conversion():
    value = float(entry.get())
    if selected_unit.get() == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
    elif selected_unit.get() == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
    result_label.config(text=f"Result: {result:.2f}")

# Function to handle time conversion
def time_conversion():
    value = float(entry.get())
    if selected_unit.get() == "Hours to Minutes":
        result = value * 60
    elif selected_unit.get() == "Minutes to Seconds":
        result = value * 60
    result_label.config(text=f"Result: {result:.2f}")

# Function to perform the appropriate conversion based on the selected category
def perform_conversion():
    if category.get() == "Length":
        length_conversion()
    elif category.get() == "Weight":
        weight_conversion()
    elif category.get() == "Temperature":
        temperature_conversion()
    elif category.get() == "Time":
        time_conversion()
    else:
        messagebox.showerror("Error", "Please select a valid category!")

# Creating the main window
window = tk.Tk()
window.title("Unit Converter")
window.geometry("400x300")

# Drop-down for conversion category
category = tk.StringVar(window)
category.set("Select Category")  # default value
category_menu = tk.OptionMenu(window, category, "Length", "Weight", "Temperature", "Time")
category_menu.pack(pady=10)

# Entry field for input value
entry_label = tk.Label(window, text="Enter value:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

# Drop-down for unit selection based on the category
selected_unit = tk.StringVar(window)
unit_menu = tk.OptionMenu(window, selected_unit, "Select Category First")
unit_menu.pack(pady=10)

# Label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)

# Button to perform the conversion
convert_button = tk.Button(window, text="Convert", command=perform_conversion)
convert_button.pack(pady=10)

# Function to update unit options based on selected category
def update_unit_options(*args):
    if category.get() == "Length":
        selected_unit.set("Meters to Kilometers")
        unit_menu["menu"].delete(0, "end")
        for option in ["Meters to Kilometers", "Kilometers to Meters", "Meters to Centimeters", "Centimeters to Meters"]:
            unit_menu["menu"].add_command(label=option, command=tk._setit(selected_unit, option))
    elif category.get() == "Weight":
        selected_unit.set("Kilograms to Grams")
        unit_menu["menu"].delete(0, "end")
        for option in ["Kilograms to Grams", "Grams to Kilograms"]:
            unit_menu["menu"].add_command(label=option, command=tk._setit(selected_unit, option))
    elif category.get() == "Temperature":
        selected_unit.set("Celsius to Fahrenheit")
        unit_menu["menu"].delete(0, "end")
        for option in ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]:
            unit_menu["menu"].add_command(label=option, command=tk._setit(selected_unit, option))
    elif category.get() == "Time":
        selected_unit.set("Hours to Minutes")
        unit_menu["menu"].delete(0, "end")
        for option in ["Hours to Minutes", "Minutes to Seconds"]:
            unit_menu["menu"].add_command(label=option, command=tk._setit(selected_unit, option))

# Bind the category selection to update unit options
category.trace("w", update_unit_options)

# Run the Tkinter event loop
window.mainloop()
