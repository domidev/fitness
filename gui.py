import tkinter as tk
from tkinter import ttk
from workout import add_workout, view_workouts
from meal import add_meal, view_meals
from database import create_database

def main_gui():
    create_database()
    root = tk.Tk()
    root.title("Fitness Tracker")
    root.geometry("400x600")
    root.configure(bg="#2e2e30")
    
    ttk.Button(root, text="Lägg till träningspass", command=add_workout).pack(pady=5)
    ttk.Button(root, text="Visa träningspass", command=view_workouts).pack(pady=5)
    ttk.Button(root, text="Lägg till maträtt", command=add_meal).pack(pady=5)
    ttk.Button(root, text="Visa maträtter", command=view_meals).pack(pady=5)
    ttk.Button(root, text="Avsluta", command=root.quit).pack(pady=5)
    
    root.mainloop()