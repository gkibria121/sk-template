from reporter.sk_report_generator import ReportGenerator
from calculator.sk_calculator import Calculator
import unittest
class TestGetValues(unittest.TestCase):

    def setUp(self):
        self.reporter =ReportGenerator()



    def test_get_values(self):

        data = {'$x': '3', '$y': '3', '$var': '460', '$var2': '6', '$xy': '12', '$yx': '18'}
        template  = '''{{$x+$y}}+{{$var+$var2}}+$xy+$yx'''
        report = self.reporter.generate_report(template,data)
        expected_report  = '3+3+460+6+$xy+$yx'
        self.assertEqual(report,expected_report)

    def test_get_values_with_expression(self):
        # Test when there is an expression in the variable declaration

        data = {'$x': '3', '$y': '3', '$z': '12'}
        template  = '''$x+$y+$z'''
        report = self.reporter.generate_report(template,data)
        expected_report  = '$x+$y+$z'
        self.assertEqual(report,expected_report)

    def test_get_values_with_multiple_expressions(self):
        # Test when there are multiple expressions in the variable declaration

        data = {'$x': '3', '$y': '3', '$z': '12', '$w': '4.5'}
        template  = '''{{$x+$y+$z+$w}}'''
        expected_report  = '3+3+12+4.5'
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_get_values_with_nested_expressions(self):
        # Test when there are nested expressions in the variable declaration
        data = "$x = 1 + 2; $y = 2 + 1; $z = $x + $y * ($x + $y); $w = $x + $y / ($x + $y);"
        data = {'$x': '3', '$y': '3', '$z': '21', '$w': '3.5'}
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_get_values(self):
        data = {'$x': '3', '$y': '3', '$var': '460', '$var2': '6', '$xy': '12', '$yx': '18'}
        template = '''{{$x+$y}}+{{$var+$var2}}+$xy+$yx'''
        report = self.reporter.generate_report(template, data)
        expected_report = '3+3+460+6+$xy+$yx'
        self.assertEqual(report, expected_report)

    def test_get_values_with_expression(self):
        data = {'$x': '3', '$y': '3', '$z': '12'}
        template = '''{{$x+$y+$z}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '3+3+12'
        self.assertEqual(report, expected_report)

    def test_get_values_with_multiple_expressions(self):
        data = {'$x': '3', '$y': '3', '$z': '12', '$w': '4.5'}
        template = '''{{$x+$y+$z+$w}}'''
        expected_report = '3+3+12+4.5'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

    def test_get_values_with_nested_expressions(self):
        data = {'$x': '3', '$y': '3', '$z': '21', '$w': '3.5'}
        template = '''{{$x + $y * ($x + $y)}} {{$x + $y / ($x + $y)}}'''
        expected_report = '3 + 3 * (3 + 3) 3 + 3 / (3 + 3)'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

    def test_get_values_with_multiple_variable_assignment(self):
        # Test when there are multiple variable assignments in the expression
        data = {'$matrix1': [1.0,2.0,3.0,4.0]}
        template = '''{{$matrix1.avg()}}'''
        expected_report = '2.5'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

    def test_get_values_with_list_variable(self):
        data = {'$list': [1, 2, 3, 4]}
        template = '''{{$list[0]}}+{{$list[1]}}+{{$list[2]}}+{{$list[3]}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '1+2+3+4'
        self.assertEqual(report, expected_report)

    def test_get_values_with_dictionary_variable(self):
        data = {'$dict': {'key1': 1, 'key2': 2, 'key3': 3}}
        template = '''{{$dict.key1}}+{{$dict.key2}}+{{$dict.key3}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '1+2+3'
        self.assertEqual(report, expected_report)

    def test_get_values_with_nested_variables(self):
        data = {'$x': '3', '$y': 3, '$z': '$x + $y'}
        template = '''{{$x}}+{{$y}}+{{$z}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '3+3+$x + $y'
        self.assertEqual(report, expected_report)


    def test_get_values_with_empty_variable(self):
        data = {'$x': '', '$y': ''}
        template = '''{{$x}}+{{$y}}'''
        report = self.reporter.generate_report(template, data)
        expected_report = '+'
        self.assertEqual(report, expected_report)


    def test_get_values_with_multiple_complex_expressions(self):
        # Test when there are multiple complex expressions in the variable declaration

        data = {'$table': [{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'department': 'Sales', 'salary': 50000.0, 'hire_date': '2020-01-15'}, {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'age': 35, 'department': 'HR', 'salary': 60000.0, 'hire_date': '2019-05-20'}, {'id': 3, 'first_name': 'Michael', 'last_name': 'Johnson', 'age': 28, 'department': 'IT', 'salary': 55000.0, 'hire_date': '2021-03-10'}, {'id': 4, 'first_name': 'Sarah', 'last_name': 'Williams', 'age': 32, 'department': 'Marketing', 'salary': 58000.0, 'hire_date': '2018-09-01'}, {'id': 5, 'first_name': 'David', 'last_name': 'Brown', 'age': 29, 'department': 'Finance', 'salary': 52000.0, 'hire_date': '2022-02-28'}]}
        template = '''{{$table[0].id}}'''
        expected_report = '''1'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$table[0].id}}'''
        expected_report = '''1'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)



    def test_get_values_with_no_variables(self):
        # Test when there are no variable declarations

        data = {'$x': [1,2,3,4,5,6,7]}
        template = '''{{$x}}'''
        expected_report='''[1, 2, 3, 4, 5, 6, 7]'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


        template = '''{{$x.avg()}}'''
        expected_report='''4.0'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.avg((x)=>x>1)}}'''
        expected_report='''4.5'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.sum()}}'''
        expected_report='''28'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.sum((x)=>x>1)}}'''
        expected_report='''27'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.min()}}'''
        expected_report='''1'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.min((x)=>x>1)}}'''
        expected_report='''2'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.count(1)}}'''
        expected_report='''1'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.count(0)}}'''
        expected_report='''0'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.len()}}'''
        expected_report='''7'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.slice(1)}}'''
        expected_report='''[2, 3, 4, 5, 6, 7]'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.slice(1,5)}}'''
        expected_report='''[2, 3, 4, 5]'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.slice(-1)}}'''
        expected_report='''[7, 6, 5, 4, 3, 2, 1]'''
        report = self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


    def test_scripts(self):
        data = {'$table': [{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'department': 'Sales', 'salary': 50000.0, 'hire_date': '2020-01-15'}, {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'age': 35, 'department': 'HR', 'salary': 60000.0, 'hire_date': '2019-05-20'}, {'id': 3, 'first_name': 'Michael', 'last_name': 'Johnson', 'age': 28, 'department': 'IT', 'salary': 55000.0, 'hire_date': '2021-03-10'}, {'id': 4, 'first_name': 'Sarah', 'last_name': 'Williams', 'age': 32, 'department': 'Marketing', 'salary': 58000.0, 'hire_date': '2018-09-01'}, {'id': 5, 'first_name': 'David', 'last_name': 'Brown', 'age': 29, 'department': 'Finance', 'salary': 52000.0, 'hire_date': '2022-02-28'}]}
        template = '''<><<{{$table[0].id}}>> </>'''
        expected_report = '''1\n'''
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''<><<{{$table[0].first_name}}>></>'''
        expected_report = '''John\n'''
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''<>
for item in {{$table}}:
    <<{item.id}>>
        </>'''
        expected_report ='1\n2\n3\n4\n5\n'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data  ={'$x': {'sanjakate': [{'allonomous': [[3]]}], 'adjectivitis': [[{'uneconomizing': [0.8498277974832624]}]], 'Galbulinae': [[{'caramba': [0.04015297797329953]}]]}}
        template = '''{{$x.sanjakate[0].allonomous[0][0]}}'''
        expected_report ='3'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_alignment(self):
        data = {'$x' : 1}
        template = '''{{$x :b}}'''
        expected_report ='1'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 1}
        template = '''{{$x :>5}}'''
        expected_report ='    1'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 1}
        template = '''{{$x :^5}}'''
        expected_report ='  1  '
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 1}
        template = '''{{$x :<5}}'''
        expected_report ='1    '
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)
        # Test case 1: Left alignment with width of 10
        data = {'$x': 123}
        template = '''{{$x :<10}}'''
        expected_report = '123       '
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

        # Test case 2: Right alignment with width of 8 and fill character '0'
        data = {'$x': 123}
        template = '''{{$x :0>8}}'''
        expected_report = '00000123'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

        # Test case 3: Center alignment with width of 6 and fill character '-'
        data = {'$x': 12}
        template = '''{{$x :-^6}}'''
        expected_report = '--12--'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

        # Test case 4: Left alignment with width of 7 and fill character '#'
        data = {'$x': 12345}
        template = '''{{$x :#<7}}'''
        expected_report = '12345##'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

        # Test case 4: Left alignment with width of 7 and fill character '#'
        data = {'$person': {'name' : 'kibria','age' : 23 , 'city' : 'Dhaka', 'country'  : 'Bangladesh'}}

        template = '''<>
for key,value in {{$person}}.items():
    <<{key:<10} : {value:<10}>>
</>'''
        expected_report ='name       : kibria    \nage        : 23        \ncity       : Dhaka     \ncountry    : Bangladesh\n'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

        data = {'$person': {'name' : 'kibria','age' : 23 , 'city' : 'Dhaka', 'country'  : 'Bangladesh'}}
        template = '''
{{$person[0]:<10}} : {{$person.name:<10}}{{$person[1]:<10}} : {{$person.age:<10}}
{{$person[2]:<10}} : {{$person.city:<10}}{{$person[3]:<10}} : {{$person.country:<10}}
'''
        self.assertEqual(report, expected_report)
        expected_report ='\nname       : kibria    age        : 23        \ncity       : Dhaka     country    : Bangladesh\n'
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)


        data ={
              "$name": "Kibria",
              "$email": "gkibria121@gmail.com",
              "$address": "123 Main Street",
              "$city": "New York",
              "$state": "NY",
              "$zip": "10001",
              "$phone": "555-123-4567",
              "$date": "July 3, 2023",
              "$recipientName": "John Smith",
              "$recipientPosition": "Human Resources Manager",
              "$organizationName": "XYZ Corporation",
              "$organizationAddress": "456 Oak Avenue",
              "$startDate": "July 10, 2023",
              "$endDate": "July 20, 2023",
              "$reason": "Family emergency",
              "$numberOfDays" : 11
            }

        template = '''
{{$name}}
{{$address}}
{{$city}}, {{$state}}, {{$zip}}
{{$email}}
{{$phone}}
{{$date}}

{{$recipientName}}
{{$recipientPosition}}
{{$organizationName}}
{{$organizationAddress}}
{{$city}}, {{$state}}, {{$zip}}

Dear {{$recipientName}},

I hope this letter finds you in good health. I am writing to formally request a leave of absence from {{$startDate}} to {{$endDate}}, as I require some personal time off. I apologize for any inconvenience this may cause and assure you that I have made arrangements to minimize the impact on my work and colleagues.

During my absence, I will make every effort to complete all pending tasks and delegate responsibilities to a trusted colleague to ensure a smooth workflow. I will also provide detailed instructions and contact information to be available for any urgent matters that may arise during my absence.

The reason for my leave is {{$reason}}. I understand the importance of my presence at work, but given the circumstances, it is essential for me to take this leave to address the situation properly.

I have reviewed the company's leave policy and believe I am entitled to {{$numberOfDays}} days of paid/unpaid leave. I would appreciate it if you could confirm this and provide any additional instructions or documentation required to process my leave request.

Please let me know if there are any specific procedures I need to follow or if there are any forms I should complete to initiate the leave request. I am more than willing to comply with any requirements and provide any necessary documentation to support my request.

I understand the impact of my absence on the team and the work at hand, and I will do my best to minimize any disruption. I am confident that my colleagues will be able to handle any urgent matters during my absence, and I will make sure to be available remotely if needed.

Thank you for your understanding and support in this matter. I value my position within the company and the opportunities it has provided me. I will be more than happy to discuss my leave further or provide any additional information you may require.

I look forward to your positive response and to returning to work rejuvenated and fully committed to my responsibilities.

Thank you once again for your attention to this matter.

Sincerely,

{{$name}}'''

        expected_report ='''
Kibria
123 Main Street
New York, NY, 10001
gkibria121@gmail.com
555-123-4567
July 3, 2023

John Smith
Human Resources Manager
XYZ Corporation
456 Oak Avenue
New York, NY, 10001

Dear John Smith,

I hope this letter finds you in good health. I am writing to formally request a leave of absence from July 10, 2023 to July 20, 2023, as I require some personal time off. I apologize for any inconvenience this may cause and assure you that I have made arrangements to minimize the impact on my work and colleagues.

During my absence, I will make every effort to complete all pending tasks and delegate responsibilities to a trusted colleague to ensure a smooth workflow. I will also provide detailed instructions and contact information to be available for any urgent matters that may arise during my absence.

The reason for my leave is Family emergency. I understand the importance of my presence at work, but given the circumstances, it is essential for me to take this leave to address the situation properly.

I have reviewed the company's leave policy and believe I am entitled to 11 days of paid/unpaid leave. I would appreciate it if you could confirm this and provide any additional instructions or documentation required to process my leave request.

Please let me know if there are any specific procedures I need to follow or if there are any forms I should complete to initiate the leave request. I am more than willing to comply with any requirements and provide any necessary documentation to support my request.

I understand the impact of my absence on the team and the work at hand, and I will do my best to minimize any disruption. I am confident that my colleagues will be able to handle any urgent matters during my absence, and I will make sure to be available remotely if needed.

Thank you for your understanding and support in this matter. I value my position within the company and the opportunities it has provided me. I will be more than happy to discuss my leave further or provide any additional information you may require.

I look forward to your positive response and to returning to work rejuvenated and fully committed to my responsibilities.

Thank you once again for your attention to this matter.

Sincerely,

Kibria'''
        report = self.reporter.generate_report(template, data)
        self.assertEqual(report, expected_report)

    def test_set(self):

        data = {'$set1' : {1,2,3,4,5,6,7} , '$set2' : {5,6,7,8,9,10}, '$set3' : {1,2,3,4,5,6,7,8,9,10}}
        template = '''{{$set1}}'''
        expected_report ='{1, 2, 3, 4, 5, 6, 7}'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$set1 - $set2}}'''
        expected_report ='{1, 2, 3, 4, 5, 6, 7} - {5, 6, 7, 8, 9, 10}'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{eval($set1 - $set2)}}'''
        expected_report ='{1, 2, 3, 4}'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_sign(self):
        data = {'$x' : 30000}
        template = '''{{$x:+d}}'''
        expected_report ='+30000'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : -30000}
        template = '''{{$x:+d}}'''
        expected_report ='-30000'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 30.123345}
        template = '''{{$x:+f}}'''
        expected_report ='+30.123345'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : -30.123345}
        template = '''{{$x:+f}}'''
        expected_report ='-30.123345'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


    def test_round(self):
        data = {'$x' : 30.123345}
        template = '''{{$x.round(2)}}'''
        expected_report ='30.12'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


        data = {'$x' : 30.123345}
        template = '''{{$x.round(4)}}'''
        expected_report ='30.1233'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 30.1299999}
        template = '''{{$x.round(3)}}'''
        expected_report ='30.13'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 30.1256789}
        template = '''{{$x.round(4)}}'''
        expected_report ='30.1257'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_format(self):

        data = {'$x': 40.6}
        template = '''{{$x:c2,fl}}
<format>
c2 = {'align': 'center','width': 10, 'fill' : 0}
fl= {'floor-significance': 2}
</format>'''
        expected_report ='40.0\n'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x': 41.9}
        template = '''{{$x:fl}}
<format>
fl= {'floor-significance': 2}
</format>'''
        expected_report ='40.0\n'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x': 40.6}
        template = '''{{$x:c2,fl}}
<format>
c2 = {'align': 'center','width': 10, 'fill' : 0}
fl= {'ceil-significance': 2}
</format>'''
        expected_report ='42.0\n'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x': 41.9}
        template = '''{{$x:fl}}
<format>
fl= {'ceil-significance': 2}
</format>'''
        expected_report ='42.0\n'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x': 40.6}
        template = '''{{$x::{'align': 'left','fill' : '#','width' : 10}}}
{{$x::{'align': 'right','fill' : '0','width' : 10,'floor-significance' : 2}}}
'''
        expected_report ='40.6######\n40.0\n'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


    def test_string(self):
        data = {'$x': '123456789'}
        template = '''{{$x::{'continue' : 5}}}'''

        expected_report ='12...'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'continue' : 2}}}'''

        expected_report ='12'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'continue' : 8}}}'''

        expected_report ='12345...'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)
        template = '''{{$x::{'continue' : 13}}}'''

        expected_report ='123456789'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x' : 'Gkibria is a great man'}
        template = '''{{$x.upper()}}'''

        expected_report ='GKIBRIA IS A GREAT MAN'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.capitalize()}}'''
        expected_report ='Gkibria Is A Great Man'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.camel()}}'''
        expected_report ='GkibriaIsAGreatMan'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.snake()}}'''
        expected_report ='gkibria_is_a_great_man'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.range(3,c)}}'''
        expected_report ='Gki'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.range(1,2)}}'''
        expected_report ='k'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.range(1,2,w)}}'''
        expected_report ='is '
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x.range(2,w)}}'''
        expected_report ='Gkibria is'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_currency(self):
        data = {'$x': '10000000'}
        template = '''{{$x::{'currency' : 'BDT'}}}'''
        expected_report ='1,00,00,000.0'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'currency' : 'USD'}}}'''
        expected_report ='10,000,000.0'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x': '10000000.1234'}
        template = '''{{$x::{'currency' : 'BDT'}}}'''
        expected_report ='1,00,00,000.12'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x': '10000000.1234'}
        template = '''{{$x::{'currency' : 'BDT', 'currency_precision' : 3}}}'''
        expected_report ='1,00,00,000.123'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x': '10000000.1234'}
        template = '''{{$x::{'currency' : 'USD', 'currency_precision' : 3}}}'''
        expected_report ='10,000,000.123'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


        data = {'$x': '1689473215.2612174'}
        template = '''{{$x::{'datetime' : '%Y-%m-%d'}}}'''
        expected_report ='2023-07-16'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : '%H:%M:%S'}}}'''
        expected_report ='08:06:55'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : '%H:%M:%S:%f'}}}'''
        expected_report ='08:06:55:261217'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : '%H:%M:%S:%f','time_precision' : 3}}}'''
        expected_report ='08:06:55:261'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : 'long'}}}'''
        expected_report ='2023:07:16 08:06:55:261217'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : 'mid'}}}'''
        expected_report ='2023:07:16 08:06 AM'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : 'short'}}}'''
        expected_report ='08:06 AM'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)



        template = '''{{$x::{'datetime' : 'long' ,'datetime_mode' : 24}}}'''
        expected_report ='2023:07:16 08:06:55:261217'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : 'mid' ,'datetime_mode' : 24}}}'''
        expected_report ='2023:07:16 08:06:55'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : 'short','datetime_mode' : 24}}}'''
        expected_report ='08:06:55'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : 'long' ,'datetime_mode' : 12}}}'''
        expected_report ='2023:07:16 08:06 AM'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : 'mid' ,'datetime_mode' : 12}}}'''
        expected_report ='2023:07:16 08:06 AM'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        template = '''{{$x::{'datetime' : 'short','datetime_mode' : 12}}}'''
        expected_report ='08:06 AM'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_scientific_notation(self):
        data = {'$x': '10000000'}
        template = '''{{$x::{'base' : 'e','precision' : '.2'}}}'''
        expected_report ='1.00e+07'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_condition(self):

        data = {'$x': {'name' : 'gkibria','age' : 24}}
        template = '''{{$x.age:c((x)=>type(x)==int),c2}}<format>
        c2 = {'align' : 'right', 'width' : 10}
        </format>'''
        expected_report ='        24'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

        data = {'$x': {'name' : 'gkibria','age' : 24}}
        template = '''{{$x.age:c((x)=>x>20),c2}}<format>
        c2 = {'align' : 'right', 'width' : 10}
        </format>'''
        expected_report ='        24'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


        data = {'$x': {'name' : 'gkibria','age' : 24}}
        template = '''{{$x.name:c((x)=>type(x)==str),c2}}<format>
        c2 = {'align' : 'right', 'width' : 10}
        </format>'''
        expected_report ='   gkibria'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)


        data = {'$x': {'name' : 'gkibria','age' : 24}}
        template = '''{{$x.name:c((x)=>x==24),c2}}<format>
        c2 = {'align' : 'right', 'width' : 10}
        </format>'''
        expected_report ='gkibria'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_condition_format(self):

        data = {'$x': 40.6}
        template = '''{{$x:c((x)=>x!=40.6),c2,fl}}
<format>
c2 = {'align': 'center','width': 10, 'fill' : 0}
fl= {'floor-significance': 2}
</format>'''
        expected_report ='40.6\n'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)
        data = {'$x': 40.6}
        template = '''{{$x:c((x)=>x!=40.6),c2,fl}}
<format>
c2 = {'align': 'center','width': 10, 'fill' : 0}
fl= {'ceil-significance': 2}
</format>'''
        expected_report ='40.6\n'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

    def test_mask(self):

        data = {'$x': 1234567890}
        template = '''{{$x:c2}}<format>
        c2 = {'mask' : '###,##,##,###'}
        </format>'''
        expected_report ='123,45,67,890'
        report =self.reporter.generate_report(template,data)
        self.assertEqual(report,expected_report)

if __name__ == '__main__':
    unittest.main()