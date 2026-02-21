import tkinter as tk
from tkinter import messagebox

class RestaurantManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Management System")

        self.menu = {
            "Burger": 180,
            "White Sauce Pasta": 250,
            "Red Sauce Pasta": 220,
            "Pizza": 280,
            "Salad": 150,
            "Coffee": 120,
            "Tea": 50,
            "Coke": 70,
            "Orange juice": 100,
            "Lemonade": 120,
        }

        self.order = {}

        self.create_menu()
        self.create_order_frame()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack(padx=10, pady=10)

        tk.Label(self.menu_frame, text="Menu", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=4)

        for i, (item, price) in enumerate(self.menu.items(), start=1):
            tk.Label(self.menu_frame, text=item).grid(row=i, column=0, sticky="w")
            tk.Label(self.menu_frame, text=f"₹{price:.2f}").grid(row=i, column=1, sticky="w")

            quantity_var = tk.IntVar(value=0)
            tk.Spinbox(self.menu_frame, from_=0, to=10, textvariable=quantity_var, width=3).grid(row=i, column=2)

            button = tk.Button(
                self.menu_frame,
                text="Add",
                command=lambda item=item, price=price, quantity_var=quantity_var: 
                self.add_to_order(item, price, quantity_var)
            )
            button.grid(row=i, column=3)

    def create_order_frame(self):
        self.order_frame = tk.Frame(self.master)
        self.order_frame.pack(padx=10, pady=10)

        tk.Label(self.order_frame, text="Order", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2)

        self.order_listbox = tk.Listbox(self.order_frame, width=40, height=10)
        self.order_listbox.grid(row=1, column=0, columnspan=2)

        self.total_label = tk.Label(self.order_frame, text="Total: ₹0.00")
        self.total_label.grid(row=2, column=0, columnspan=2)

        tk.Button(self.order_frame, text="Calculate Bill", command=self.calculate_bill)\
            .grid(row=3, column=0, columnspan=2, pady=5)

    def add_to_order(self, item, price, quantity_var):
        quantity = quantity_var.get()

        if quantity > 0:
            if item in self.order:
                self.order[item][0] += quantity
            else:
                self.order[item] = [quantity, price]

            self.update_order_listbox()
            messagebox.showinfo("Success", f"{quantity} {item}(s) added to order.")

    def update_order_listbox(self):
        self.order_listbox.delete(0, tk.END)
        total = 0

        for item, (quantity, price) in self.order.items():
            total += quantity * price
            self.order_listbox.insert(tk.END, f"{item}: {quantity} x ₹{price:.2f}")

        self.total_label.config(text=f"Total: ₹{total:.2f}")

    def calculate_bill(self):
        if not self.order:
            messagebox.showwarning("Empty Order", "No items added to the order.")
            return

        total = sum(quantity * price for quantity, price in self.order.values())

        bill_text = "Restaurant Bill\n\n"
        for item, (quantity, price) in self.order.items():
            bill_text += f"{item}: {quantity} x ₹{price:.2f}\n"
        bill_text += f"\nTotal: ₹{total:.2f}"

        messagebox.showinfo("Bill", bill_text)


def main():
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
