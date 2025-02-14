import sqlite3
from tkinter import messagebox

#Tar bort en post från databasen.
def delete_entry(table, entry_id):
    conn = sqlite3.connect('fitness.db')
    c = conn.cursor()
    c.execute(f"DELETE FROM {table} WHERE id = ?", (int(entry_id),))
    conn.commit()
    conn.close()
    messagebox.showinfo("Lyckat", "Posten raderad!")
