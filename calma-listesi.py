class Sarki:
    def __init__(self, sarkiİsmi, sanatci):
        self.sarkiİsmi = sarkiİsmi
        self.sanatci = sanatci

    def sarkiGoster(self):
        print(f"Şarkının ismi: {self.sarkiİsmi} Sanatçı: {self.sanatci}")


class CalmaListesi:
    def __init__(self):
        self.sarkilar = []

    def sarkiEkle(self, sarki):
        self.sarkilar.append(sarki)
        print(f"{sarki.sarkiİsmi} isimli şarkı çalma listesine eklendi")

    def sarkiCikar(self, sarkiIsmi):
        sarkiBulundu = False 
        for i in self.sarkilar:
            if i.sarkiİsmi == sarkiIsmi:
                self.sarkilar.remove(i)
                sarkiBulundu = True
                break  
        
        if not sarkiBulundu:
            print(f"{sarkiIsmi} isimli şarkı bulunamadı")

    def sarkilariGoster(self):
        if not self.sarkilar:
            print("Çalma listesinde şarkı yok")
        else:
            for i in self.sarkilar:
                i.sarkiGoster()



sarki1 = Sarki("Without Me", "Eminem")
sarki2 = Sarki("Houdini", "Eminem")
sarki3 = Sarki("Drop It Like It's Hot", "Snoop Dogg")


calma_listesi = CalmaListesi()


calma_listesi.sarkiEkle(sarki1)
calma_listesi.sarkiEkle(sarki2)
calma_listesi.sarkiEkle(sarki3)


calma_listesi.sarkiCikar("Houdini")


calma_listesi.sarkilariGoster()