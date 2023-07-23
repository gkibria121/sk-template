import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat
from sk_report_generator.reporter.formatter.custom_format_functions.mask import Mask
from sk_report_generator.reporter.formatter.custom_format_functions.mask import GetPattern
from sk_report_generator.reporter.formatter.custom_format_functions.mask import EvaluateMask




class TestMask(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.mask = Mask()
        self.mask.set_successor(self.default)

    def test_mask(self):
        value = 10000000
        format_spec =  {'mask' : '#,##,##,#,##'}

        value = 10000000
        format_spec =  {'mask' : '#,#'}

        result = self.mask.format(value,format_spec)
        self.assertEqual(result, '1,00,00,00,0')

        value = 100.01
        format_spec =  {'mask' : '(###)#(##)'}

        result = self.mask.format(value,format_spec)
        self.assertEqual(result, '(100).(01)')


        value = 100.123456789
        format_spec =  {'mask' : '(###)#(#########)'}

        result = self.mask.format(value,format_spec)
        self.assertEqual(result, '(100).(123456789)')

        value = +8801521254580
        format_spec =  {'mask' : '+(##) ###########'}

        result = self.mask.format(value,format_spec)
        self.assertEqual(result, '+(88) 01521254580')


class TestGetPattern(unittest.TestCase):

    def setUp(self):
        self.get_pattern = GetPattern()

    def test_mask(self):
        mask = '(##) ####'
        result = self.get_pattern.run(mask)
        self.assertEqual(result[0],'([\\d\\.]{2})([\\d\\.]{4})')
        self.assertEqual(result[1],'(\\1) \\2')

        mask = '+(##) ###########'
        result = self.get_pattern.run(mask)
        self.assertEqual(result[0],'([\\d\\.]{2})([\\d\\.]{11})')
        self.assertEqual(result[1],'+(\\1) \\2')

        mask = '(###)#(#########)'
        result = self.get_pattern.run(mask)
        self.assertEqual(result[0],'([\\d\\.]{3})([\\d\\.]{1})([\\d\\.]{9})')
        self.assertEqual(result[1],'(\\1)\\2(\\3)')

        mask = '#,##,##,#,##'
        result = self.get_pattern.run(mask)
        self.assertEqual(result[0],'([\\d\\.]{1})([\\d\\.]{2})([\\d\\.]{2})([\\d\\.]{1})([\\d\\.]{2})')
        self.assertEqual(result[1],'\\1,\\2,\\3,\\4,\\5')
class TestEvaluateMask(unittest.TestCase):

    def setUp(self):
        self.eval = EvaluateMask()

    def test_mask(self):

        value = '8801521254580'
        pattern ='([\\d\\.]{2})([\\d\\.]{11})'
        replace = '+(\\1) \\2'
        result = self.eval.run(value,pattern,replace)
        self.assertEqual(result,'+(88) 01521254580')



        pattern ='([\\d\\.]{3})([\\d\\.]{1})([\\d\\.]{9})'
        replace='(\\1)\\2(\\3)'
        result = self.eval.run(value,pattern,replace)
        self.assertEqual(result,'(880)1(521254580)')


        pattern ='([\\d\\.]{1})([\\d\\.]{2})([\\d\\.]{2})([\\d\\.]{1})([\\d\\.]{2})'
        replace = '\\1,\\2,\\3,\\4,\\5'
        result = self.eval.run(value,pattern,replace)
        self.assertEqual(result,'8,80,15,2,1254580')

if __name__ == "__main__":
    unittest.main()