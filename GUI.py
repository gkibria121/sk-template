import tkinter as tk
from tkinter import ttk, scrolledtext
from packages.calculator.sk_calculator import Calculator
from packages.data.sk_data_handler.data import DataStructure
from packages.reporter.sk_report_generator import ReportGenerator
from packages.variable.sk_variable_handler.variable_handler import VariableHandler
from packages.random_variable.sk_random_variable import RandomVariableGenerator
from packages.table.sk_table_hanlder import TableHandler
import traceback
import json

class TinkerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #config

        self.calculator = Calculator()
        self.data_structure = DataStructure()
        self.variable = VariableHandler()
        self.random = RandomVariableGenerator()
        self.table_handler = TableHandler()
        self.reporter = ReportGenerator()
        self.reporter.set_reporter(self.reporter)

        self.variable.set_calculator(self.calculator)

        self.data_structure.set_random(self.variable)
        self.data_structure.set_variable(self.random)
        self.data_structure.set_table_handler(self.table_handler)



        #app

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
        self.ds = scrolledtext.ScrolledText(self.tab_data_structure)
        self.ds.pack(fill='both', expand=True)

    def create_error_logs_tab(self):
        # Add content for the "Reporter" tab here
        label = tk.Label(self.error_logs, text="Errors",state='disabled')
        label.pack(padx=10, pady=10)
        self.errors =scrolledtext.ScrolledText(self.error_logs)
        self.errors.pack(fill='both', expand=True)

    def create_variable_declaration_tab(self):
        # Add content for the "Variable Declaration" tab here
        label = tk.Label(self.tab_variable_declaration, text="Write Script")
        label.pack(padx=10, pady=10)
        self.variable_text = scrolledtext.ScrolledText(self.tab_variable_declaration)
        self.variable_text.pack(fill='both', expand=True)
        button = tk.Button(self.tab_variable_declaration,text='Generate Data',command=self.get_data,padx=10,pady=10)
        button.pack(pady=10)

    def create_template_tab(self):
        # Add content for the "Template" tab here
        label = tk.Label(self.tab_template, text="Insert Template")
        label.pack(padx=10, pady=10)
        self.template = scrolledtext.ScrolledText(self.tab_template)
        self.template.pack(fill='both', expand=True)
        button = tk.Button(self.tab_template, text='Generate Report', command=self.generate_report, padx=10, pady=10)
        button.pack(side='bottom', pady=10)
    def create_report_tab(self):
        # Add content for the "Report" tab here
        label = tk.Label(self.tab_report, text="Report")
        label.pack(padx=10, pady=10)
        self.report = tk.Text(self.tab_report,state='disabled')
        self.report.pack(fill='both', expand=True)


    def generate_report(self):
        template = self.template.get("1.0", "end-1c")
        variable = self.variable_text.get("1.0", "end-1c")

        data =self.check_error( eval,(self.ds.get("1.0", "end-1c")),self.tab_template)

        report = self.check_error(self.reporter.generate_report,(template, data),self.tab_report)

        self.report.configure(state='normal')  # Enable editing of the report tab
        self.report.delete(1.0, tk.END)  # Clear previous content
        self.report.insert(tk.END, report)  # Insert processed content
        self.report.configure(state='disabled')


    def get_data(self):
        variable = self.variable_text.get("1.0", "end-1c")

        data_stucture = self.check_error( self.data_structure.run,variable,self.tab_data_structure)
        self.ds.delete(1.0, tk.END)  # Clear previous content
        formated_data_structure = json.dumps(data_stucture,indent=4)
        self.ds.insert(tk.END, formated_data_structure)  # Insert processed content

    def write_error(self,error):
        self.errors.configure(state='normal')  # Enable editing of the report tab
        self.errors.delete(1.0, tk.END)  # Clear previous content
        self.errors.insert(tk.END, f"\n{error}",'red_tag')  # Insert processed content
        self.errors.tag_configure('red_tag', foreground='red')
        self.errors.configure(state='disabled')

    def check_error(self, function, arguments,redirect):
        try:
            if type( arguments) != tuple:
                result =function(arguments)
            else:
                result = function(*arguments)
            self.tab_control.tab(4, text="Error Logs")
            self.errors.configure(state='normal')  # Enable editing of the report tab
            self.errors.delete(1.0, tk.END)  # Clear previous content
            self.errors.configure(state='disabled')
            self.tab_control.select(redirect)
            return result
        except Exception as error:
            error = traceback.format_exc()
            self.write_error(str(error))
            self.tab_control.tab(4, text="Error Logs ⚠️")
            self.tab_control.select(self.error_logs)
            return 'Check Error Logs'






if __name__ == "__main__":
    app = TinkerApp()
    app.mainloop()
