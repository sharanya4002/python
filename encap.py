class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def display(self):
        print(self.name,self.role)
class company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):
        print("hiring the manager role")

c=company('wipro','hyd')
e= Employee('sharanya','deveop',85000)
e.display()
c.comdisplay()
print(c._hiring())

        
