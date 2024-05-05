from tkinter import * 
from tkinter import messagebox

def raise_frame(frame):
    home_frame.pack_forget()
    main_frame.pack_forget()
    frame.pack(fill="both", expand=True, padx=10, pady=10)
count = 0
btn_stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

def display_choice(state, button):
    global count, btn_stats
    count += 1
    
    if count % 2 == 0:
        button.config(text="O")
        btn_stats[state] = 10
    else:
        button.config(text="X")
        btn_stats[state] = 11
    
    # Define winning conditions
    winning_conditions = [
        # Rows
        (btn_stats[1], btn_stats[2], btn_stats[3]),
        (btn_stats[4], btn_stats[5], btn_stats[6]),
        (btn_stats[7], btn_stats[8], btn_stats[9]),
        # Columns
        (btn_stats[1], btn_stats[4], btn_stats[7]),
        (btn_stats[2], btn_stats[5], btn_stats[8]),
        (btn_stats[3], btn_stats[6], btn_stats[9]),
        # Diagonals
        (btn_stats[1], btn_stats[5], btn_stats[9]),
        (btn_stats[3], btn_stats[5], btn_stats[7]),
    ]
    
    # Check winning conditions for Player 1 (X)
    for condition in winning_conditions:
        if condition.count(11) == 3:
            main_label.config(text="Player 1 Victory!!!")
            return
    
    # Check winning conditions for Player 2 (O)
    for condition in winning_conditions:
        if condition.count(10) == 3:
            main_label.config(text="Player 2 Victory!!!")
            return
    
    # Check for a tie
    if all(value in [10, 11] for value in btn_stats.values()):
        main_label.config(text="It's a Tie!!!")

def restart_game(buttons):
    global count, btn_stats
    btn_stats = {key: 0 for key in btn_stats}
    count=0
    main_label.config(text="Tic-Tac-Toe")
    for button in buttons:
        button.config(text="")

    

def main():

    root = Tk()
    root.title("Tic Tac Toe")
    root.geometry("700x550")
    root.configure(bg="#e27602")

    logo = PhotoImage(file="logo.png")
    root.iconphoto(True, logo)

    def exit_game():
        expire = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if expire:
            root.quit()

    global home_frame
    home_frame = Frame(root, bg="#e27602")
    global main_frame
    main_frame = Frame(root, bg="#e27602")

    home_custom_font = ("Times", 28, "bold italic")
    home_label = Label(home_frame, text="Tic-Tac-Toe", font=home_custom_font, bg="#e27602", fg="#420f00")
    home_label.pack(fill="both", expand=True, pady=20)

    btn_font = ("Arial", 16, "bold")
    home_button1 = Button(home_frame, text="START GAME", command=lambda: raise_frame(main_frame), width=20, font=btn_font, fg="#f1ee8e", bg="#e88904", activebackground="#e27602", activeforeground="#f1ee8e")
    home_button1.pack(fill="both", expand=True, pady=40, padx=10)

    home_button2 = Button(home_frame, text="QUIT GAME", command=exit_game, width=20, font=btn_font, fg="#f1ee8e", bg="#e88904", activebackground="#e27602", activeforeground="#f1ee8e")
    home_button2.pack(fill="both", expand=True, pady=20, padx=10)

    global main_label
    main_custom_font = ("Times", 24, "bold italic")
    main_label = Label(main_frame, text="Tic-Tac-Toe", font=main_custom_font, bg="#e27602", fg="#420f00")
    main_label.grid(row=0, columnspan=3, sticky="nsew")

    for i in range(5):  # Set weight for rows
        main_frame.rowconfigure(i, weight=1)
    for i in range(3):  # Set weight for columns
        main_frame.columnconfigure(i, weight=1)

    button_font = (("Arial", 24, "bold"))
    main_button1 = Button(main_frame, text="", command=lambda: display_choice(1, main_button1), font=button_font, width=10, height=2)
    main_button1.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    main_button2 = Button(main_frame, text="", command=lambda: display_choice(2, main_button2), font=button_font, width=10, height=2)
    main_button2.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    main_button3 = Button(main_frame, text="", command=lambda: display_choice(3, main_button3), font=button_font, width=10, height=2)
    main_button3.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
    main_button4 = Button(main_frame, text="", command=lambda: display_choice(4, main_button4), font=button_font, width=10, height=2)
    main_button4.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
    main_button5 = Button(main_frame, text="", command=lambda: display_choice(5, main_button5), font=button_font, width=10, height=2)
    main_button5.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
    main_button6 = Button(main_frame, text="", command=lambda: display_choice(6, main_button6), font=button_font, width=10, height=2)
    main_button6.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
    main_button7 = Button(main_frame, text="", command=lambda: display_choice(7, main_button7), font=button_font, width=10, height=2)
    main_button7.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
    main_button8 = Button(main_frame, text="", command=lambda: display_choice(8, main_button8), font=button_font, width=10, height=2)
    main_button8.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
    main_button9 = Button(main_frame, text="", command=lambda: display_choice(9, main_button9), font=button_font, width=10, height=2)
    main_button9.grid(row=3, column=2, sticky="nsew", padx=5, pady=5)

    buttons = (main_button1, main_button2, main_button3, main_button4, main_button5, main_button6, main_button7, main_button8, main_button9)
    restart_button = Button(main_frame, text="RESTART GAME", command=lambda: restart_game(buttons), font=btn_font, fg="#f1ee8e", bg="#e88904", activebackground="#e27602", activeforeground="#f1ee8e", width=20, height=3)
    restart_button.grid(row=4, columnspan=3, pady=10, sticky="nsew")
    exit_button = Button(main_frame, text="QUIT GAME", command=exit_game, font=btn_font, fg="#f1ee8e", bg="#e88904", activebackground="#e27602", activeforeground="#f1ee8e", width=20, height=3)
    exit_button.grid(row=5, columnspan=3, pady=10, sticky="nsew")

    home_frame.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()
if __name__ == "__main__":
    main()
