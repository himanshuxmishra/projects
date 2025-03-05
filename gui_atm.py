import tkinter as tk
from tkinter import messagebox
# Initial pin and balance
pin_num = 1111
balance = 1000000
def check_pin():
    entered_pin = pin_entry.get()
    try:
        entered_pin = int(entered_pin)
        if entered_pin == pin_num:
            pin_frame.pack_forget()  
            options_frame.pack()  
        else:
            messagebox.showerror("Error", "Invalid PIN!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid PIN!")
def check_balance():
    messagebox.showinfo("Balance", f"Your balance is: {balance}")
def withdraw():
    withdraw_window = tk.Toplevel(root)
    withdraw_window.title("Withdraw Money")
    withdraw_window.geometry("300x200")
    withdraw_window.configure(bg="lightgray")
    withdraw_label = tk.Label(withdraw_window, text="Enter amount to withdraw:", font=("Arial", 14), bg="lightgray")
    withdraw_label.pack(pady=10)
    withdraw_entry = tk.Entry(withdraw_window, font=("Arial", 14), width=20)
    withdraw_entry.pack(pady=10)
    def process_withdraw():
        global balance  
        try:
            withdraw_amount = int(withdraw_entry.get())
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                messagebox.showinfo("Success", f"Withdrawal successful! Remaining balance: {balance}")
                withdraw_window.destroy()
            else:
                messagebox.showerror("Error", "Insufficient funds!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")
    withdraw_button = tk.Button(withdraw_window, text="Withdraw", font=("Arial", 14), bg="orange", fg="white", command=process_withdraw)
    withdraw_button.pack(pady=10)
root = tk.Tk()
root.title("ATM")
root.geometry("400x500")  
root.configure(bg="lightgray")
header_label = tk.Label(root, text="ATM Machine", font=("Algerian", 24, "bold"), bg="blue", fg="white", pady=20)
header_label.pack(fill="both")
pin_frame = tk.Frame(root, bg="lightgray")
pin_frame.pack(padx=10, pady=50)
pin_label = tk.Label(pin_frame, text="Enter Pin Number:", font=("Arial", 14), bg="lightgray")
pin_label.pack(pady=10)
pin_entry = tk.Entry(pin_frame, show="*", font=("Arial", 14), width=20)
pin_entry.pack(pady=10)
pin_button = tk.Button(pin_frame, text="Login", font=("Arial", 14), bg="blue", fg="white", command=check_pin)
pin_button.pack(pady=10)
options_frame = tk.Frame(root, bg="lightgray")
option_label = tk.Label(options_frame, text="Select an option:", font=("Arial", 16), bg="lightgray")
option_label.pack(pady=10)
check_balance_button = tk.Button(options_frame, text="Check Balance", font=("Arial", 14), bg="green", fg="white", command=check_balance)
check_balance_button.pack(pady=10, fill="both")
withdraw_button = tk.Button(options_frame, text="Withdraw", font=("Arial", 14), bg="orange", fg="white", command=withdraw)
withdraw_button.pack(pady=10, fill="both")
root.mainloop()