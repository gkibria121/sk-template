import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.json_dumps import Dumps
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat




class TestFloor(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.dumps = Dumps()
        self.dumps.set_successor(self.default)

    def test_floor(self):
        value = '{"key" : "value"}'
        format_spec =  {'dumps' : True}

        result = self.dumps.format(value,format_spec)
        self.assertEqual(result, '{\n    "key": "value"\n}')

        format_spec =  {'dumps' : False}

        result = self.dumps.format(value,format_spec)
        self.assertEqual(result, '{"key" : "value"}')

        format_spec =  {'dumps' : True , 'intent' : 5}

        result = self.dumps.format(value,format_spec)
        self.assertEqual(result, '{\n     "key": "value"\n}')

        format_spec =  {'dumps' : False , 'intent' : 5}

        result = self.dumps.format(value,format_spec)
        self.assertEqual(result, '{"key" : "value"}')

        format_spec = { 'intent' : 5}

        result = self.dumps.format(value,format_spec)
        self.assertEqual(result, '{\n     "key": "value"\n}')
if __name__ == "__main__":
    unittest.main()