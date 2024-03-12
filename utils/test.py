
from ramatcals_class import ramatcals

ramatcal1 = ramatcals('bouboun', 12, '10/10/2022', '10/10/2028')

jsonString = ramatcal1.to_json()

ramatcal1.ramatcals_to_json('jsonfile',jsonString)
