import sqlite3
from tkinter import simpledialog, messagebox, ttk, Toplevel, Button
import pandas as pd

def add_meal():
    date = simpledialog.askstring("Lägg till maträtt", "Ange datum (YYYY-MM-DD):")
    name = simpledialog.askstring("Lägg till maträtt", "Ange maträttens namn:")
    calories = simpledialog.askinteger("Lägg till maträtt", "Ange kalorier:")
    protein = simpledialog.askinteger("Lägg till maträtt", "Ange protein (g):")
    carbs = simpledialog.askinteger("Lägg till maträtt", "Ange kolhydrater (g):")
    fat = simpledialog.askinteger("Lägg till maträtt", "Ange fett (g):")
    
    if date and name and calories and protein and carbs and fat:
        conn = sqlite3.connect('fitness.db')
        c = conn.cursor()
        c.execute("INSERT INTO meals (date, name, calories, protein, carbs, fat) VALUES (?, ?, ?, ?, ?, ?)", (date, name, calories, protein, carbs, fat))
        conn.commit()
        conn.close()
        messagebox.showinfo("Lyckat", "Maträtt tillagd!")

def delete_meal(meal_id, tree):
    conn = sqlite3.connect('fitness.db')
    c = conn.cursor()
    c.execute("DELETE FROM meals WHERE id = ?", (meal_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Maträtt raderad!")
    tree.delete(*tree.get_children())
    view_meals()

def view_meals():
    conn = sqlite3.connect('fitness.db')
    c = conn.cursor()
    c.execute("SELECT * FROM meals")
    records = c.fetchall()
    conn.close()
    
    df = pd.DataFrame(records, columns=["ID", "Datum", "Namn", "Kalorier", "Protein", "Kolhydrater", "Fett"])
    total_calories = df["Kalorier"].sum()
    
    messagebox.showinfo("Statistik", f"Totala kalorier: {total_calories}")

    view_win = Toplevel()
    view_win.title("Visa Maträtter")
    tree = ttk.Treeview(view_win, columns=("ID", "Datum", "Namn", "Kalorier", "Protein", "Kolhydrater", "Fett"), show='headings')
    
    for col in ["ID", "Datum", "Namn", "Kalorier", "Protein", "Kolhydrater", "Fett"]:
        tree.heading(col, text=col)
    
    for record in df.itertuples(index=False):
        tree.insert("", "end", values=record)
    
    tree.pack()
    
    Button(view_win, text="Radera markerad", command=lambda: delete_meal(tree.item(tree.selection())['values'][0], tree)).pack()