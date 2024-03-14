class Talaba:
    '''Talaba nomli klass yaratamiz'''
    def __init__(self, ism, familya, tyil):
        """Talabaning xususyatlari"""
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    
    def tanishtir(self):
        print(f"Isim: {self.ism} {self.familya} {self.tyil}")
    
talaba1 = Talaba("Daston", "Radjapov", 1993)
talaba2 = Talaba("Mardon", "Radjapov", 1995)
talaba3 = Talaba("Otabek", "Abdukarimov", 1997)
    
talaba1.get_name()

# talaba1.tanishtir()
# talaba2.tanishtir()
# talaba3.tanishtir()

    
    
    