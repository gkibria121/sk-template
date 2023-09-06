import unittest
from sk_function_solver.function.foreach import Foreach
from sk_function_solver.function.default import MethodDefault
from sk_report_generator import ReportGenerator

class TestForeach(unittest.TestCase):

    def setUp(self):
        self.foreach = Foreach()
        self.default = MethodDefault()
        self.reporter = ReportGenerator()
        self.reporter.set_reporter(self.reporter)
        self.foreach.set_reporter(self.reporter)
        data = {'$x' : [{"name": "John Doe","age": 30,"occupation": "Engineer"},{"name": "Jane Smith","age": 25,"occupation": "Teacher"},{"name": "Michael Johnson","age": 40, "occupation": "Doctor"},{"name": "Emily Williams","age": 22,"occupation": "Student"}],
        '$y' : [[{'name' : 'gkibria'},{'name' : 'mehedi'}]] , '$z': [[[{'name' : 'gkibria'},{'name' : 'mehedi'}]]]}
        self.foreach.set_data(data)
        self.foreach.set_next(self.default)

    def test_foreach(self):

        value = [{"name": "John Doe","age": 30,"occupation": "Engineer"},{"name": "Jane Smith","age": 25,"occupation": "Teacher"},{"name": "Michael Johnson","age": 40, "occupation": "Doctor"},{"name": "Emily Williams","age": 22,"occupation": "Student"}]
        method = 'foreach'
        condition ='($y)=>{{{$y.name}}}'
        result = self.foreach.run(value,method,condition)
        self.assertEqual(result,'John DoeJane SmithMichael JohnsonEmily Williams')

        method = 'foreach'
        condition ='($y)=>{{{$y.age }}}'
        result = self.foreach.run(value,method,condition)
        self.assertEqual(result,'30 25 40 22 ')

        value =[[{'name' : 'gkibria'},{'name' : 'mehedi'}]]
        method = 'foreach'
        condition ='($z)=>{ {{$z.foreach(($a)=>{ {{$a}} })}} }'
        result = self.foreach.run(value,method,condition)
        self.assertEqual(result,"  {'name': 'gkibria'}  {'name': 'mehedi'}  ")


        value =[[[{'name' : 'gkibria'},{'name' : 'mehedi'}]]]
        method = 'foreach'
        condition ='($a)=>{ {{$a.foreach(($b)=>{ {{$b.foreach(($c)=>{ {{$c}} } )}} })}} }'
        result = self.foreach.run(value,method,condition)
        self.assertEqual(result,"   {'name': 'gkibria'}  {'name': 'mehedi'}   ")

if __name__=='__main__':
    unittest.main()