class  business:
    #static data
    name ='SR cosmetics'
    def __init__(self,nofsales,nofpro,address,email):
        
        self.nofsales=nofsales
        self.nofpro=nofpro
        self.address=address
        self.email=email
    '''def display(self):
        print('business name :',business.name)
        print('no.of.sales are:',self.nofsales)
        print('no.of.products manufactured:',self.nofpro)
        print('address : ',self.address)
        print('email is : ',self.email)'''
    def __str__(self):
        return f'{business.name} {self.nofsales} {self.nofpro} {self.address} {self.email}'
b=business(5000,8000,'hyd','sharanya@gmail.com')
b1=business(7000,10000,'banglore','anshu@gmail.com')
print(b)
print(b1)

