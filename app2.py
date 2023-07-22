import tkinter as tk
from tkinter import ttk
from calculator.sk_calculator import Calculator
from variable.sk_variable_handler.variable_handler import VariableHandler
from reporter.sk_report_generator import ReportGenerator
from declaration.sk_declaration import DeclarationGenerator


class TinkerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.variable = VariableHandler()
        self.variable.set_calculator(self.calculator)
        self.reporter = ReportGenerator()
        self.declaration_process = DeclarationGenerator()

        self.title("Reporting Template")
        self.geometry("800x600")

        self.tab_control = ttk.Notebook(self)

        # Create and add tabs to the tab_control
        self.tab_report = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_report, text="Report",padding = 5)

        self.tab_template = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_template, text="Template",padding = 5)

        self.tab_variable_declaration = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_variable_declaration, text="Script",padding = 5)

        self.tab_data_structure = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_data_structure, text="Data Structure",padding = 5)

        self.error_logs = ttk.Frame(self.tab_control)
        self.tab_control.add(self.error_logs, text="Error Logs",padding = 5)

        self.tab_control.pack(fill=tk.BOTH, expand=1)

        self.create_report_tab()
        self.create_template_tab()
        self.create_variable_declaration_tab()
        self.create_error_logs_tab()
        self.create_ds_tab()

    def create_ds_tab(self):
        label = tk.Label(self.tab_data_structure, text = "Data Structure")
        label.pack(padx=10,pady=10)
        self.ds = tk.Text(self.tab_data_structure )
        self.ds.pack(fill='both', expand=True)

    def create_error_logs_tab(self):
        # Add content for the "Reporter" tab here
        label = tk.Label(self.error_logs, text="Reporter Tab Content",state='disabled')
        label.pack(padx=10, pady=10)
        self.errors = tk.Text(self.error_logs)
        self.errors.pack(fill='both', expand=True)

    def create_variable_declaration_tab(self):
        # Add content for the "Variable Declaration" tab here
        label = tk.Label(self.tab_variable_declaration, text="Write Script")
        label.pack(padx=10, pady=10)
        self.variable_text = tk.Text(self.tab_variable_declaration)
        self.variable_text.pack(fill='both', expand=True)
        button = tk.Button(self.tab_variable_declaration,text='Generate Data',command=self.get_data,padx=10,pady=10)
        button.pack(pady=10)

    def create_template_tab(self):
        # Add content for the "Template" tab here
        label = tk.Label(self.tab_template, text="Insert Template")
        label.pack(padx=10, pady=10)
        self.template = tk.Text(self.tab_template)
        self.template.pack(fill='both', expand=True)

    def create_report_tab(self):
        # Add content for the "Report" tab here
        label = tk.Label(self.tab_report, text="Report")
        label.pack(padx=10, pady=10)
        self.report = tk.Text(self.tab_report,state='disabled')
        self.report.pack(fill='both', expand=True)
        button = tk.Button(self.tab_report,text='Generate Report',command=self.generate_report,padx=10,pady=10)
        button.pack(pady=10)

    def generate_report(self):
        template = self.template.get("1.0", "end-1c")
        variable = self.variable_text.get("1.0", "end-1c")
        data = eval(self.ds.get("1.0", "end-1c"))

        report = self.reporter.generate_report(template, data)
        self.report.configure(state='normal')  # Enable editing of the report tab
        self.report.delete(1.0, tk.END)  # Clear previous content
        self.report.insert(tk.END, report)  # Insert processed content
        self.report.configure(state='disabled')

    def get_data(self):
        variable = self.variable_text.get("1.0", "end-1c")
        data_stucture = self.variable.get_result(self.declaration_process.process(variable))
        self.ds.delete(1.0, tk.END)  # Clear previous content
        self.ds.insert(tk.END, data_stucture)  # Insert processed content


if __name__ == "__main__":
    app = TinkerApp()
    app.mainloop()
