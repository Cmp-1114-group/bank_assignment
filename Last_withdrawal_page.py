def open2():
    def withdraw():
        balance = float(ent_initial.get())
        amount = float(ent_wit.get())
        if balance >= amount:
            balance -= amount
            lbl_result['text'] = ("Withdrawal successful.")
        else:
            lbl_result['text'] = ("Insufficient balance.")

    ent_initial = tk.Entry(master=frame, width=10)
    lbl_initial = tk.Label(master=frame, width=10, text="initial amount")
    ent_wit = tk.Entry(master=frame, width=10)
    lbl_wit = tk.Label(master=frame, text="Amount")
    lbl_result = tk.Label(master=frame, text="")
    ent_initial.grid(row=0, column=1)
    lbl_initial.grid(row=0, column=0)
    lbl_wit.grid(row=2, column=0,  padx=10, pady=10)
    ent_wit.grid(row=3, column=0,  padx=10, pady=10)
    btn_withdraw2 = tk.Button(master=frame, command=withdraw, text="withdraw")
    btn_withdraw2.grid(row=4, column=0, padx=10, pady=10)
    lbl_result.grid(row=5, column=0, padx=10, pady=10)
