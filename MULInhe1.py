from abc import ABC
class mobiles(ABC):
    def andriod():
        print("andriod operating system")
    def features():
        pass
class vivo(mobiles):
    def features():
        print("high storage")
class oppo(mobiles):
    def features():
        print("high quality camera")
class samsung(mobiles):
    def features():
        print("Inbulit AI")
print("--------VIVO---------")
v=vivo
v.features()
v.andriod()
print("-------OPPO-----------")
o=oppo
o.features()
o.andriod()
print("-------SAMSUNG---------")
s=samsung
s.features()
s.andriod()
    
