class Floor:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='floor':

            if condition =='':
                value =math.floor(value)
            else:
                precision = float(condition)
                value = float(value)
                mod = value % precision

                if mod == 0:
                    value = str(value)
                else:
                    value = str(value  - mod)

        return self.go_next.run(value,method,condition)