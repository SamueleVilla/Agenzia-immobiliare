# main module python


from Agenzia.agency import Agenzia
from Agenzia.models import *

myAgenzy = Agenzia("Villa cars & motors", "Milano")

casa = Immobile("1234AADD", "Via Riviera 18", 28053, "Roma", 500)
mybox = Box("AADDAAEE", "Via Riviera 18", 2798, "Roma", 200, 10)
myApart = Appartamento("AAEE12445", "Via caduti per la libertà 69",
                       9876, "Roma", 400, 6, 2)
myvilla = Villa("KKJAAD22", "Via dei ricconi 32",
                2976, "Milano", 1000, 10, 7, 500)

myAgenzy.add_immobile(casa)
myAgenzy.add_immobile(mybox)
myAgenzy.add_immobile(myApart)
myAgenzy.add_immobile(myvilla)

for immobile in myAgenzy.search_immobili("Via Riviera 18"):
    print(immobile.scheda_immobile(), end="\n\n")

# end and it works :)
