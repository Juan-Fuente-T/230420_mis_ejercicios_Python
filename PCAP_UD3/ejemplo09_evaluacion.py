class Programa:
    pass
class Serie(Programa):
    pass
class MiniSerie(Serie):
    pass
ms = MiniSerie

print(isinstance (ms, MiniSerie))
print(isinstance (ms, Serie))
print(isinstance (ms, Programa))
print(isinstance (ms, object))
print(isinstance (ms, list))#False
#Ver el del profe