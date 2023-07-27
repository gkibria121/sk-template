import unittest
from sk_report_generator.reporter.function_solver.function.foreach import Foreach
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
from sk_report_generator import ReportGenerator

class TestForeach(unittest.TestCase):

    def setUp(self):
        self.foreach = Foreach()
        self.default = MethodDefault()
        self.reporter = ReportGenerator()
        self.foreach.set_reporter(self.reporter)


        self.foreach.set_next(self.default)

    def test_foreach(self):
        data = {'$x' : [{"name": "John Doe","age": 30,"occupation": "Engineer"},{"name": "Jane Smith","age": 25,"occupation": "Teacher"},{"name": "Michael Johnson","age": 40, "occupation": "Doctor"},{"name": "Emily Williams","age": 22,"occupation": "Student"}]}
        self.foreach.set_data(data)
        value = '$x'
        method = 'foreach'
        condition ='($y)=>{{{$y}}}'
        print(self.foreach.run(value,method,condition))

if __name__=='__main__':
    unittest.main()