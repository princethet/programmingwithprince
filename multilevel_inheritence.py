class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"YES i dance {self.dance} no of times."

class Grandson(Son):
    dance = 7

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes i dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

#print(harry.isdance())
print(harry.basketball)
