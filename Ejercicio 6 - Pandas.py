import pandas as pd
datos = {"a": 10, "b" : 20, "c": 30, "d":40, "f": 60}
serie = pd.Series(datos)
print (serie)
print (serie ["a"])
print (serie ["b"])