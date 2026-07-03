import tkinter as tk
from calculator.operations import add, subtract, multiply, divide

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        
        # Current expression string
        self.expression = ""
        
        # Display Screen
        self.display_var = tk.StringVar()
        self.create_display()
        
        # Buttons Grid Layout
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#f4f4f4")
        display_frame.pack(expand=True, fill="both")
        
        display_label = tk.Label(
            display_frame, 
            textvariable=self.display_var, 
            anchor="e", 
            font=("Arial", 28), 
            bg="#f4f4f4", 
            padx=15
        )
        display_label.pack(expand=True, fill="both")

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")
        
        # Matrix layout definition
        button_layouts = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']    # For the perfect empty space alignment
        ]
        
        # Configure grid weight so buttons expand evenly
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.columnconfigure(j, weight=1)

        for row_idx, row in enumerate(button_layouts):
            for col_idx, char in enumerate(row):
                if char == '':       # Skip empty space
                    continue
                
                # Dynamic styling for operator buttons
                bg_color = "#e0e0e0"
                if char in ['/', '*', '-', '+', '=']:
                    bg_color = "#ff9f0a"  # Calculator orange
                elif char == 'C':
                    bg_color = "#a5a5a5"
                
                # Perfect alignment logic
                column_span = 1
                if char == '0':
                    # Let 0 take up two columns neatly
                    column_span = 2
                
                
                actual_col = col_idx
                if char == '.':
                    actual_col = 2
                elif char == '=' and row_idx == 4:
                    actual_col = 3

                btn = tk.Button(
                    buttons_frame, 
                    text=char, 
                    font=("Arial", 18), 
                    bg=bg_color, 
                    borderwidth=1,
                    command=lambda x=char: self.on_button_click(x)
                )
                btn.grid(row=row_idx, column=actual_col, columnspan=column_span, sticky="nsew")

                
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
        elif char == '=':
            self.calculate_result()
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)

    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.display_var.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set("Error: Div by 0")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

def run_calculator():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()