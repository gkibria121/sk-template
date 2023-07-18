import tkinter as tk
from tkinter import ttk
from calculator.sk_calculator import Calculator
from variable.sk_variable_handler.variable_handler import VariableHandler
from reporter.sk_report_generator import ReportGenerator
from declaration.sk_declaration import DeclarationGenerator


class TinkerApp(tk.Frame):
    def __init__(self, master):
        self.calculator = Calculator()
        self.variable = VariableHandler()
        self.variable.set_calculator(self.calculator)
        self.reporter = ReportGenerator()
        self.declaration_process = DeclarationGenerator()

        super().__init__(master)
        self.master = master
        self.configure(width=600, height=300)

        self.tab_control = tk.ttk.Notebook(self)

        self.tab_main = tk.Frame(self.tab_control)

        self.tab_control.add(self.tab_main, text="Report")

        self.variable_label = tk.Label(self.tab_main, text="Declare Variables")
        self.variable_entry = tk.Text(self.tab_main, height=10)

        self.variable_ds_label = tk.Label(self.tab_main, text="Data Structure")
        self.variable_ds_text = tk.Text(self.tab_main, height=10)

        self.template_label = tk.Label(self.tab_main, text="Template:")
        self.template_entry = tk.Text(self.tab_main, height=12)

        self.report_label = tk.Label(self.tab_main, text="Report:")
        self.report_text = tk.Text(self.tab_main, height=12)

        self.button = tk.Button(self.tab_main, text="Generate Report", command=self.generate_report, height=2)

        self.variable_label.grid(row=0, column=1)
        self.variable_entry.grid(row=1, column=1, sticky="ns")  # Set sticky="ns" for vertical expansion

        self.variable_ds_label.grid(row=0, column=2)
        self.variable_ds_text.grid(row=1, column=2, sticky="ns")  # Set sticky="ns" for vertical expansion

        self.template_label.grid(row=5, column=0)
        self.template_entry.grid(row=5, column=1, sticky="nsew", columnspan=2)  # Set sticky="ns" for vertical expansion

        self.report_label.grid(row=10, column=0)
        self.report_text.grid(row=10, column=1, sticky="nsew", columnspan=2)

        self.button.grid(row=15, column=0, columnspan=3)

        self.rowconfigure(3, weight=1, minsize=20)  # Allow row 2 (report_text) to expand vertically
        self.columnconfigure(2, weight=1)  # Allow column 1 (template_entry and variable_entry) to expand horizontally

        self.tab_control.pack(fill=tk.BOTH, expand=1)
        self.pack()  # Add this line to display the frame

    def generate_report(self):
        template = self.template_entry.get("1.0", tk.END)
        variable = self.variable_entry.get("1.0", tk.END)

        data = self.variable.get_result(self.declaration_process.process(variable))
        self.variable_ds_text.delete(1.0, tk.END)
        self.variable_ds_text.insert(1.0, data)

        report = self.reporter.generate_report(template, data)

        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(1.0, report)


def main():
    root = tk.Tk()
    app = TinkerApp(root)
    app.mainloop()


if __name__ == "__main__":
    main()
