import sqlite3
import pandas as pd
from tkinter import simpledialog, messagebox, ttk, Toplevel, Button

def add_workout():
    date = simpledialog.askstring("Lägg till träningspass", "Ange datum (YYYY-MM-DD):")
    type = simpledialog.askstring("Lägg till träningspass", "Ange träningsaktivitet:")
    duration = simpledialog.askinteger("Lägg till träningspass", "Ange varaktighet (minuter):")
    calories = simpledialog.askinteger("Lägg till träningspass", "Ange förbrukade kalorier:")
    
    if date and type and duration and calories:
        conn = sqlite3.connect('fitness.db')
        c = conn.cursor()
        c.execute("INSERT INTO workouts (date, type, duration, calories) VALUES (?, ?, ?, ?)", (date, type, duration, calories))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Träningspass tillagt!")

def delete_selected(tree):
    """Tar bort markerad rad från databasen och GUI."""
    selected_item = tree.selection()  # Hämtar markerad rad i Treeview
    if not selected_item:
        messagebox.showwarning("Ingen vald", "Vänligen välj en post att radera.")
        return

    # Hämtar ID:t från den markerade raden
    entry_id = tree.item(selected_item, "values")[0]

    # Bekräfta borttagning
    confirm = messagebox.askyesno("Bekräfta", f"Är du säker på att du vill radera ID {entry_id}?")
    if not confirm:
        return

    # Radera från databasen
    conn = sqlite3.connect('fitness.db')
    c = conn.cursor()
    c.execute("DELETE FROM workouts WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()

    # Radera från GUI
    tree.delete(selected_item)
    messagebox.showinfo("Lyckat", "Posten raderad!")

def view_workouts():
    """Visar träningspass i ett GUI och låter användaren radera poster."""
    conn = sqlite3.connect('fitness.db')
    c = conn.cursor()
    c.execute("SELECT * FROM workouts")
    records = c.fetchall()
    conn.close()
    
    # Skapa en Pandas DataFrame
    df = pd.DataFrame(records, columns=["ID", "Datum", "Typ", "Varaktighet", "Kalorier"])
    
    view_win = Toplevel()
    view_win.title("Visa Träningspass")

    tree = ttk.Treeview(view_win, columns=("ID", "Datum", "Typ", "Varaktighet", "Kalorier"), show='headings')
    for col in ["ID", "Datum", "Typ", "Varaktighet", "Kalorier"]:
        tree.heading(col, text=col)
    
    for record in df.itertuples(index=False):
        tree.insert("", "end", values=record)

    tree.pack()

    delete_button = Button(view_win, text="Radera markerad post", command=lambda: delete_selected(tree))
    delete_button.pack()