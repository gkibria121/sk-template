import unittest

from sk_report_generator.reporter.formatter.process.get_condition import GetCondition


class TestGetCondition(unittest.TestCase):

    def setUp(self):
        self.get_condition = GetCondition()

    def test_align(self):
        value = '2'
        format_spec ='((x)=>x>1),c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,True)

        value = 2
        format_spec ='((x)=>x>1),c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,True)

        value = 1
        format_spec ='((x)=>x>1),c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,False)

        value = 1
        format_spec ='((x)=>x>=1),c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,True)


        value = 1
        format_spec ='((x)=> x>1 or x==1),c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,True)

        value = -1
        format_spec ='((x)=> x>1 or x==1),c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,False)

        value = 'gkibria'
        format_spec ='((x)=>  x=="gkibria"),c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,True)


        value = 'gkibria'
        format_spec ='((x)=>  x!="gkibria"),c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,False)

        value = 'gkibria'
        format_spec ='((x)=>  len(x))>5,c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,True)

        value = '[1,2,3,4,5,6]'
        format_spec ='((x)=>  max(x))>5,c2'
        result = self.get_condition.run(value,format_spec)
        self.assertEqual(result,True)


if __name__ == '__main__':
    unittest.main()