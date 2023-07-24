import unittest

from sk_report_generator.reporter.formatter.process.format_tag_remove import FormatTagRemover


class TestFormatTagRemove(unittest.TestCase):

    def setUp(self):
        self.format_tag_remove = FormatTagRemover()

    def test_align(self):

        template = '''<format> something</format>'''
        result = self.format_tag_remove.run(template)
        self.assertEqual(result,'')

        template = '''<format> something



        </format>'''
        result = self.format_tag_remove.run(template)
        self.assertEqual(result,'')

        template = '''<format> something



        </format> '''
        result = self.format_tag_remove.run(template)
        self.assertEqual(result,' ')


        template = ''' <format> something



        </format> '''
        result = self.format_tag_remove.run(template)
        self.assertEqual(result,'  ')

        template = ''' <format> something
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        </format> '''
        result = self.format_tag_remove.run(template)
        self.assertEqual(result,'  ')

if __name__ == '__main__':
    unittest.main()