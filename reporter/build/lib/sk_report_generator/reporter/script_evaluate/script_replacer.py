import regex as re


class ScriptReplacer:

    def __init__(self):
        pass

    def run(self, template, script_results):
        for scripts, results in script_results:
            template = re.sub(re.escape(scripts, results), results, template)

        return template
