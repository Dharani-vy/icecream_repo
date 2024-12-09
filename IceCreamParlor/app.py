import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_PATH = 'C:/Users/DHARANI/Desktop/IceCreamParlor/ice_cream_parlor.db'

# Database utility functions
def connect_db():
    """Connect to the SQLite database."""
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def fetch_flavors(search_term=""):
    """Fetch flavors matching the search term."""
    conn = connect_db()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        query = "SELECT name, season FROM flavors WHERE name LIKE ?"
        cursor.execute(query, ('%' + search_term + '%',))
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        results = []
    finally:
        conn.close()
    return results

# Application class
class IceCreamParlorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ice Cream Parlor")
        self.root.geometry("600x500")

        self.cart = []

        # Search Frame
        self.search_label = tk.Label(root, text="Search Flavors:", font=("Arial", 14))
        self.search_label.pack(pady=10)

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var, font=("Arial", 12))
        self.search_entry.pack(pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_flavors, font=("Arial", 12))
        self.search_button.pack(pady=5)

        self.flavor_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
        self.flavor_listbox.pack(pady=5)

        # Add to Cart Button
        self.add_to_cart_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart, font=("Arial", 12))
        self.add_to_cart_button.pack(pady=5)

        # Cart Frame
        self.cart_label = tk.Label(root, text="Your Cart:", font=("Arial", 14))
        self.cart_label.pack(pady=10)

        self.cart_listbox = tk.Listbox(root, width=50, height=5, font=("Arial", 12))
        self.cart_listbox.pack(pady=5)

    def search_flavors(self):
        """Search and display matching flavors."""
        search_term = self.search_var.get().strip()
        if not search_term:
            messagebox.showinfo("Info", "Please enter a flavor name to search")
            return

        flavors = fetch_flavors(search_term)
        self.flavor_listbox.delete(0, tk.END)  # Clear the listbox

        if flavors:
            for flavor in flavors:
                self.flavor_listbox.insert(tk.END, f"{flavor[0]} ({flavor[1]})")
        else:
            messagebox.showinfo("Info", "No matching flavors found")

    def add_to_cart(self):
        """Add selected flavor to the cart."""
        selected = self.flavor_listbox.get(tk.ACTIVE)
        if selected:
            if selected not in self.cart:
                self.cart.append(selected)
                self.cart_listbox.insert(tk.END, selected)
                messagebox.showinfo("Success", f"{selected} added to the cart!")
            else:
                messagebox.showinfo("Info", "Item already in cart")
        else:
            messagebox.showinfo("Info", "Please select an item to add")

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamParlorApp(root)
    root.mainloop()
