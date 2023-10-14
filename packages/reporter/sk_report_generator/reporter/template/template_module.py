from pathlib import Path
import regex as re
class Moduler:
    def __init__(self):
        self.get_files = GetFilesFromFolder()
        self.path = ''
        self.replace_template_reference = ReplaceFileReference()
        self.replace_placeholder_variable = ReplacePlaceHolderVariable()
        self.replace_placeholder_variable.set_next( self.replace_template_reference)
        self.replace_template_reference.set_next(type('Default',(),{'run' : lambda template,files: template}))

    def report(self, template):
        template_path = self.path
        if template_path != '':
            files = self.get_files.run(template_path)

            template = self.replace_placeholder_variable.run(template,files)

        return self.successor.report(template)

    def set_successor(self, successor):
        self.successor = successor


    def set_data(self, data):
        self.data = data

    def set_path(self,path):
        self.path = path



class GetFilesFromFolder:

    def run(self,path,sub=''):
        folder_path = Path(f"{path}") if sub=='' else Path(path+sub)
        files ={}
        for item in folder_path.iterdir():
            if item.is_file():
                if item.name.endswith('.tmpl') or  item.name.endswith('.txt'):
                    name = item.name if sub =='' else sub+'/'+item.name
                    name = re.sub('(.txt)|(.tmpl)|(^/)','',name)
                    files[name] = item.read_text()

            elif item.is_dir() and not str(item).startswith('.'):
                files.update(self.run(path,sub+'/'+item.name))

        return files

class ReplaceFileReference:

    def run(self,template,files):

        pattern = r'{{\s*\:\:([\w\/]+)\s*(,\s*({([^{}]|(?3))*}))?}}'
        template = re.sub(pattern , lambda match: files[match[1]],template)

        return self.go_next.run(template,files)

    def set_next(self,go_next):
        self.go_next = go_next

class ReplacePlaceHolderVariable:

    def run(self,template,files):

        pattern =  r'{{\s*\:\:([\w\/]+)\s*(,\s*({([^{}]|(?3))*}))?}}'
        matches = re.findall(pattern,template)
        for match in matches:
            if match[2]!='':
                variables = eval(match[2])
                file = match[0]
                content = files[file]
                for key,value in variables.items():

                    content = re.sub(re.escape(key)+r'(?>\b)',value,content)

                files[file] = content


        return self.go_next.run(template,files)

    def set_next(self,go_next):
        self.go_next = go_next


