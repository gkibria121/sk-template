import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.datetime import Time
from sk_report_generator.reporter.formatter.custom_format_functions.datetime import LongDate
from sk_report_generator.reporter.formatter.custom_format_functions.datetime import ShortDate
from sk_report_generator.reporter.formatter.custom_format_functions.datetime import MidDate
from sk_report_generator.reporter.formatter.custom_format_functions.datetime import Defualt
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat




class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.time = Time()
        self.time.set_successor(self.default)

    def test_time(self):

        value = '1689473215.2612174'
        format_spec = {'datetime' : '%Y-%m-%d'}
        expected_result ='2023-07-16'
        result =self.time.format(value,format_spec)
        self.assertEqual(result,expected_result)

        format_spec = {'datetime' : '%H:%M:%S'}
        expected_result ='08:06:55'
        result =self.time.format(value,format_spec)
        self.assertEqual(result,expected_result)

        format_spec = {'datetime' : '%H:%M:%S:%f'}
        expected_result ='08:06:55:261217'
        result =self.time.format(value,format_spec)
        self.assertEqual(result,expected_result)

        format_spec = {'datetime' : '%H:%M:%S:%f','time_precision' : 3}
        expected_result ='08:06:55:261'
        result =self.time.format(value,format_spec)
        self.assertEqual(result,expected_result)




class TestLongDate(unittest.TestCase):

    def setUp(self):
        self.default = Defualt()
        self.long = LongDate()
        self.long.set_next(self.default)

    def test_long(self):

        value = 1689473215.2612174
        format_spec = {'datetime' : 'long'}
        expected_result ='2023:07:16 08:06:55:261217'
        result =self.long.run(value,format_spec)
        self.assertEqual(result,expected_result)

        format_spec = {'datetime' : 'long' ,'datetime_mode' : 24}
        expected_result ='2023:07:16 08:06:55:261217'
        result =self.long.run(value,format_spec)
        self.assertEqual(result,expected_result)

        format_spec = {'datetime' : 'long' ,'datetime_mode' : 12}
        expected_result ='2023:07:16 08:06 AM'
        result =self.long.run(value,format_spec)
        self.assertEqual(result,expected_result)

class TestMidDate(unittest.TestCase):

    def setUp(self):
        self.default = Defualt()
        self.mid = MidDate()
        self.mid.set_next(self.default)

    def test_mid(self):

        value = 1689473215.2612174

        format_spec = {'datetime' : 'mid'}
        expected_result ='2023:07:16 08:06 AM'
        result =self.mid.run(value,format_spec)
        self.assertEqual(result,expected_result)

        format_spec = {'datetime' : 'mid' ,'datetime_mode' : 24}
        expected_result ='2023:07:16 08:06:55'
        result =self.mid.run(value,format_spec)
        self.assertEqual(result,expected_result)


        format_spec = {'datetime' : 'mid' ,'datetime_mode' : 12}
        expected_result ='2023:07:16 08:06 AM'
        result =self.mid.run(value,format_spec)
        self.assertEqual(result,expected_result)


class TestShortDate(unittest.TestCase):

    def setUp(self):
        self.default = Defualt()
        self.short = ShortDate()
        self.short.set_next(self.default)

    def test_short(self):

        value = 1689473215.2612174


        format_spec = {'datetime' : 'short'}
        expected_result ='08:06 AM'
        result =self.short.run(value,format_spec)
        self.assertEqual(result,expected_result)


        format_spec = {'datetime' : 'short','datetime_mode' : 24}
        expected_result ='08:06:55'
        result =self.short.run(value,format_spec)
        self.assertEqual(result,expected_result)

        format_spec = {'datetime' : 'short','datetime_mode' : 12}
        expected_result ='08:06 AM'
        result =self.short.run(value,format_spec)
        self.assertEqual(result,expected_result)


if __name__ == "__main__":
    unittest.main()