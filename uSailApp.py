import tkinter as tk
from tkinter import ttk  # For modern widgets like Combobox

app = tk.Tk()
app.title("uSail 1.0b Charleston")
app.geometry("500x600")

# Create frames
navFrame = tk.Frame(app, bg="darkgrey")
weatherFrame = tk.Frame(app, bg="pink")
appFrame = tk.Frame(app, bg="midnightblue")

# Boat type frame inside the appFrame
boatTypeFrame = tk.Frame(appFrame, bg="lightblue")
boatTypeFrame.pack(pady=10, fill="x")

# Store frames in a list
frames = [appFrame, navFrame, weatherFrame]

# Function to show a frame
def show_frame(frame):
    # Hide all frames
    for F in frames:
        F.pack_forget()
    # Show the selected frame
    frame.pack(fill="both", expand=True)

# Menu Frame (Stays at the top)
menuFrame = tk.Frame(app, bg="grey")
menuFrame.pack(side="top", fill="x", pady=5)  # Ensures it always stays at the top

# Configure columns in the menu frame
menuFrame.columnconfigure(0, weight=1)
menuFrame.columnconfigure(1, weight=1)
menuFrame.columnconfigure(2, weight=1)
menuFrame.columnconfigure(3, weight=1)

# Add buttons to the menu frame
homeButton = tk.Button(
    menuFrame,
    text="Home",
    font=('Arial', 10),
    bg="darkgrey",
    fg="white",
    command=lambda: show_frame(appFrame)
)
homeButton.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5)

NavMenuButton = tk.Button(
    menuFrame,
    text="Nav",
    font=('Arial', 10),
    bg="darkgrey",
    fg="white",
    command=lambda: show_frame(navFrame)
)
NavMenuButton.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5)

WeatherMenuButton = tk.Button(
    menuFrame,
    text="Weather",
    font=('Arial', 10),
    bg="darkgrey",
    fg="white",
    command=lambda: show_frame(weatherFrame)
)
WeatherMenuButton.grid(row=0, column=2, sticky=tk.W + tk.E, padx=5)

CalculateButton = tk.Button(
    menuFrame,
    text="Calculate Route",
    font=('Arial', 10),
    bg="green",
    fg="white",
    command=lambda: show_frame(weatherFrame)  # Update this with a frame specific to calculations
)
CalculateButton.grid(row=0, column=3, sticky=tk.W + tk.E, padx=5)

# Home screen content
homeMenuText = tk.Label(
    appFrame,
    bg="midnightblue",
    fg="white",
    text="Welcome to uSail - Version Charleston 1.0 Beta",
    font=("Arial", 14)
)
homeMenuText.pack(pady=20)

boatTypePrompt = tk.Label(
    boatTypeFrame,
    bg="lightblue",
    text="Please select your boat type:",
    font=("Arial", 12)
)
boatTypePrompt.pack(pady=10)

# Dropdown menu for boat types
boat_types = ["Laser", "Beneteau", "Jeanneau", "Catalina Yachts", "Kraken Yachts"]
selected_boat_type = tk.StringVar()
boatTypeDropdown = ttk.Combobox(
    boatTypeFrame,
    textvariable=selected_boat_type,
    values=boat_types,
    state="readonly",
    font=("Arial", 10)
)
boatTypeDropdown.set("Select Boat Type")
boatTypeDropdown.pack(pady=5)

# Entry for boat model
boatModelPrompt = tk.Label(
    boatTypeFrame,
    bg="lightblue",
    text="Enter your boat model:",
    font=("Arial", 12)
)
boatModelPrompt.pack(pady=5)

boat_model = tk.StringVar()
boatModelEntry = tk.Entry(
    boatTypeFrame,
    textvariable=boat_model,
    font=("Arial", 10)
)
boatModelEntry.pack(pady=5)

# Entry for year
yearPrompt = tk.Label(
    boatTypeFrame,
    bg="lightblue",
    text="Enter the year of your boat:",
    font=("Arial", 12)
)
yearPrompt.pack(pady=5)

boat_year = tk.StringVar()
yearEntry = tk.Entry(
    boatTypeFrame,
    textvariable=boat_year,
    font=("Arial", 10)
)
yearEntry.pack(pady=5)

# Entry for ft length
lengthPrompt = tk.Label(
    boatTypeFrame,
    bg="lightblue",
    text="Enter the length of your boat (in ft):",
    font=("Arial", 12)
)
lengthPrompt.pack(pady=5)

boat_length = tk.StringVar()
lengthEntry = tk.Entry(
    boatTypeFrame,
    textvariable=boat_length,
    font=("Arial", 10)
)
lengthEntry.pack(pady=5)

# Submit Button
def submit_boat_type():
    selected = selected_boat_type.get()
    model = boat_model.get()
    year = boat_year.get()
    length = boat_length.get()

    if selected == "Select Boat Type":
        resultLabel.config(text="Please select a valid boat type.")
    elif not model.strip():
        resultLabel.config(text="Please enter a valid boat model.")
    elif not year.strip() or not year.isdigit():
        resultLabel.config(text="Please enter a valid year.")
    elif not length.strip() or not length.isdigit():
        resultLabel.config(text="Please enter a valid length (in ft).")
    else:
        resultLabel.config(
            text=(f"Boat Type: {selected}\n"
                  f"Model: {model}\n"
                  f"Year: {year}\n"
                  f"Length: {length} ft")
        )

submitButton = tk.Button(
    boatTypeFrame,
    text="Submit",
    font=("Arial", 10),
    bg="darkblue",
    fg="white",
    command=submit_boat_type
)
submitButton.pack(pady=10)

# Result Label for feedback
resultLabel = tk.Label(boatTypeFrame, bg="lightblue", font=("Arial", 10))
resultLabel.pack(pady=5)

# Show the initial frame
show_frame(appFrame)

app.mainloop()
