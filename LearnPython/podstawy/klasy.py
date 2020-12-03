class car:
    name_lib = ('skoda', 'merc')
    name = ''
    type = ''
    color = ''
    cost = 100
    def opis(self):
        opis_auta = ('%s to %s %s wart %.2f' % (self.name, self.color, self.type, self.cost))
        return opis_auta

auto1 = car()
Auto2 = car()

auto1.name = 'skoda'
Auto2.name = 'BMW'
if auto1.name in auto1.name_lib:
    print("auto w lib")
else:
    print ('brak auta')

auto1.cost = 10.12
Auto2.cost = 323423.12
auto1.type = 'sedan'
Auto2.type = 'kabrio'
auto1.color = 'czerwone'
Auto2.color = 'czarne'

print(auto1.opis())
print(Auto2.opis())
