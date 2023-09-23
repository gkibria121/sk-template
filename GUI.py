import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
from packages.calculator.sk_calculator import Calculator
from packages.data.sk_data_handler.data import DataStructure
from packages.reporter.sk_report_generator import ReportGenerator
from packages.variable.sk_variable_handler.variable_handler import VariableHandler
from packages.random_variable.sk_random_variable import RandomVariableGenerator
from packages.table.sk_table_hanlder import TableHandler
from packages.wrapper.sk_mongo_wrapper.sk_mongo_wrapper import MongoWrapper
from packages.controller.sk_mongo_controller.sk_mongo_controller import MongoController
from packages.function.sk_function_solver.function_solver import FunctionSolver
from packages.function.sk_function_solver.process_function_calling import ProcessFunctionCalling
from packages.function.sk_function_solver.single_function_solver import SingleFunctionSOlver
from packages.function.sk_function_solver.get_index_value import GetIndexValue
from packages.function.sk_function_solver.process_condition import ProcessCondition
import tkinter.font as tk_font
import traceback
import json
import regex as re
class TinkerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #config

        self.calculator = Calculator()
        self.data_structure = DataStructure()
        self.variable = VariableHandler()
        self.variable.set_function_solver(FunctionSolver())

        self.random = RandomVariableGenerator()
        self.table_handler = TableHandler()
        self.function_solver =FunctionSolver()
        self.mongo_controller = MongoController()
        self.mongo_wrapper = MongoWrapper()
        self.table_handler.set_wrapper(self.mongo_wrapper)
        self.table_handler.set_mongo_controller(self.mongo_controller)


        self.reporter = ReportGenerator()
        self.reporter.set_function_solver(self.function_solver)
        self.reporter.set_reporter(self.reporter)

        self.variable.set_calculator(self.calculator)

        self.data_structure.set_variable(self.variable)
        self.data_structure.set_random(self.random)
        self.data_structure.set_table_handler(self.table_handler)
        self.function_solver.set_ds_solver_chain(self.data_structure.comment_remover)
        self.data_structure.set_function_solver(self.function_solver)


        #app

        self.title("Reporting Template")
        self.geometry("800x600")
        # Create a header frame
        self.header_frame = tk.Frame(self)
        self.header_frame.pack(fill=tk.X)

        # Add header widgets
        self.header_label = tk.Label(self.header_frame, text='Untitled', font=("Helvetica", 12))
        self.header_label.pack(pady=2)



        # Create a vertical sidebar
        self.sidebar = tk.Frame(self, width=10)
        self.sidebar.pack(fill=tk.Y, side=tk.LEFT,pady=100)

        self.tab_control = ttk.Notebook(self)
        # Create and add tabs to the tab_control
        self.tab_report = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_report, text="Report",padding = 5)

        self.tab_names = ["Report", "Template", "Script", "Data Structure", "Error Logs"]
        self.tab_buttons = []
        for idx, tab_name in enumerate(self.tab_names):
            button = tk.Button(self.sidebar, text=tab_name, command=lambda idx=idx: self.switch_tab(idx),height=3)
            button.pack(fill=tk.X, pady=5)




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
        # Create a menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create a "File" menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu", menu=file_menu)

        # Add "Open File" option to the "File" menu
        file_menu.add_command(label="New File", command=self.new_file)
        file_menu.add_command(label="Open File", command=self.open_file)

        # Add "Save File" option to the "File" menu
        file_menu.add_command(label="Save File", command=self.save_file)
        file_menu.add_command(label="Save As File", command=self.save_as_file)

        # Hide the tabs in the top bar
        style = ttk.Style(self)
        style.layout("TNotebook.Tab", [])  # Hide the tabs
        self.footer_frame = tk.Frame(self)
        self.footer_frame.pack(fill=tk.X)
        # Add footer widgets
        self.footer_lable = tk.Label(self.footer_frame, text='', font=("Helvetica", 12), anchor="w")
        self.footer_lable.pack(pady=2)
        self.bind("<Control-'>", self.add_comment)


    def switch_tab(self, idx):
        self.tab_control.select(idx)
    def create_ds_tab(self):
        label = tk.Label(self.tab_data_structure, text = "Data Structure")
        label.pack(padx=10,pady=10)
        self.ds = scrolledtext.ScrolledText(self.tab_data_structure,background='lightgrey')
        self.ds.pack(fill='both', expand=True)
    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.file_name  = re.search(r'(\w+)\.\w+',self.file_path)[1]
        self.set_header_name(self.file_name)
        self.set_footer_name(self.file_path)
        if self.file_path:
            with open(self.file_path, "r") as file:
                file_contents = file.read()
            # Insert file contents into the currently active text widget
            script = re.search(r'<script>([\s\S]*)<\/script>',file_contents)
            self.variable_text.delete(1.0, tk.END)
            if script:
                self.variable_text.insert(tk.END,script[1])

            template = re.search(r'<template>([\s\S]*)<\/template>',file_contents)

            self.template.delete(1.0, tk.END)
            if template:
                self.template.insert(tk.END,template[1])
        self.get_data()
        self.generate_report()

    def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if  self.file_path:
            file_contents = ''
            file_contents += f'<template>{self.template.get("1.0", "end-1c")}</template>'
            file_contents += f'\n<script>{self.variable_text.get("1.0", "end-1c")}</script>'


            if file_contents != '':
                self.file_path = self.file_path if  self.file_path.endswith('.txt') else  self.file_path+'.txt'
                with open(self.file_path, "w") as file:
                    file.write(file_contents)
    def save_file(self):
        if self.file_path:
            file_contents = ''
            file_contents += f'<template>{self.template.get("1.0", "end-1c")}</template>'
            file_contents += f'\n<script>{self.variable_text.get("1.0", "end-1c")}</script>'


            if file_contents != '':
                self.file_path = self.file_path if self.file_path.endswith('.txt') else  self.file_path+'.txt'
                with open(self.file_path, "w") as file:
                    file.write(file_contents)
        if self.file_path==None:
            self.save_as_file()
    def new_file(self):
        self.file_path = None
        self.set_header_name('Untitled')
        self.errors.delete(1.0,tk.END)
        self.variable_text.delete(1.0,tk.END)
        self.template.delete(1.0,tk.END)
        self.report.configure(state='normal')  # Enable editing of the report tab
        self.report.delete(1.0, tk.END)  # Clear previous content
        self.report.configure(state='disabled')
        self.ds.delete(1.0,tk.END)

    def add_comment(self, event):
        # Get the current cursor position
        current_window =  self.get_selected_box(self.tab_control.select())
        cursor_position = current_window.index(tk.INSERT)
        value = ''
        if current_window in [self.variable_text]:
            try:
                text = current_window.get("sel.first", "sel.last")
                current_window.delete("sel.first", "sel.last")
            except tk.TclError:
                new_line_index = cursor_position.split('.')[0]+'.0'
                text =current_window.get(new_line_index,cursor_position)
                current_window.delete(new_line_index,cursor_position)
            value = self.toggle_comment(text)
            # Add a comment at the cursor position
            comment_text = current_window
            current_window.insert(cursor_position, value)

    def toggle_comment(self,value):


        pattern = r'(\n|^)#'
        match = re.search(pattern,value)
        print(value)
        if match:
            return re.sub(pattern,lambda match : match[1],value)

        value = re.sub('(\n|^)',lambda match : match[1]+'#',value)

        return value






    def get_selected_box(self,box):

        index = self.tab_control.index(box)
        selected_tab =self.tab_control.winfo_children()[index]
        selected_tab_str = str(selected_tab)

        if  selected_tab_str == '.!notebook.!frame':

            return self.report

        elif  selected_tab_str == '.!notebook.!frame2':
            return self.template

        elif selected_tab_str == '.!notebook.!frame3':
            return self.variable_text

        elif  selected_tab_str == '.!notebook.!frame4':
            return self.ds

        elif  selected_tab_str == '.!notebook.!frame5':
            return self.errors




        return 1


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
        self.variable_text = scrolledtext.ScrolledText(self.tab_variable_declaration,background='lightgrey',undo=True)
        self.variable_text.pack(fill='both', expand=True)
        button = tk.Button(self.tab_variable_declaration,text='Generate Data',command=self.get_data,padx=10,pady=10)
        button.pack(pady=10)
    def create_template_tab(self):
        # Add content for the "Template" tab here
        label = tk.Label(self.tab_template, text="Insert Template")
        label.pack(padx=10, pady=10)
        self.template = scrolledtext.ScrolledText(self.tab_template,undo=True)
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
##            error = traceback.format_exc()
##            print(error)
            self.write_error(str(error))
            self.tab_control.tab(4, text="Error Logs ⚠️")
            self.tab_control.select(self.error_logs)
            return 'Check Error Logs'

    def set_header_name(self,new_name):
        self.header_label.config(text=new_name)

    def set_footer_name(self,new_name):
        self.footer_lable.config(text=new_name)
if __name__ == "__main__":
    app = TinkerApp()
    app.mainloop()
