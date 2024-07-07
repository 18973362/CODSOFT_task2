import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("320x320")  

        self.current_input = ""
        self.display = tk.Entry(master, width=22, font=('Arial', 24), borderwidth=5, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.display.insert(0, "0")

        

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('C', 4, 0), ('=', 4, 2)
        ]

        for (text, row, col) in buttons:
            self.add_button(text, row, col)

        

    def add_button(self, text, row, col):
        button_command = lambda: self.on_button_click(text)
        tk.Button(self.master, text=text, width=9, height=3, font=('Arial', 12), command=button_command).grid(row=row, column=col, sticky="nsew")

        tk.Grid.columnconfigure(self.master, col, weight=1)
        tk.Grid.rowconfigure(self.master, row, weight=1)

    def on_button_click(self, char):
        
        if char == 'C':
            self.current_input = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                self.current_input = str(eval(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(0, self.current_input)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.current_input += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_input)
        

    

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()