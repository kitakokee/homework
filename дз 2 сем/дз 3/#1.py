#1. Реализовать класс  бор с методами добавления, поиска и удаления

class Bor: 

    def __init__(self):
        self.koren = {} 

    def dobavit(self, slovo):
        tekushiy_uzel = self.koren
        for bukva in slovo:
            if bukva not in tekushiy_uzel:
                tekushiy_uzel[bukva] = {}  
            tekushiy_uzel = tekushiy_uzel[bukva] 
        tekushiy_uzel['#'] = True  
    def poisk(self, slovo):
        tekushiy_uzel = self.koren
        for bukva in slovo:
            if bukva not in tekushiy_uzel:
                return False
            tekushiy_uzel = tekushiy_uzel[bukva] 
        return '#' in tekushiy_uzel

    def udalit(self, slovo): 
        if not self.poisk(slovo):
            return  

        tekushiy_uzel = self.koren
        put = [] 

        for bukva in slovo:
            put.append((tekushiy_uzel, bukva)) 
            tekushiy_uzel = tekushiy_uzel[bukva]

        del tekushiy_uzel['#'] 
        for uzel, bukva in reversed(put): 
            if not uzel[bukva]: 
                del uzel[bukva]
            else:
                break  


