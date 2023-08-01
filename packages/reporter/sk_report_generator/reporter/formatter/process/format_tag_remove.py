import regex as re


class FormatTagRemover:

    def run(self, template):
        pattern = r'<format>[\s\S]*?</format>'
        return re.sub(pattern,'',template)