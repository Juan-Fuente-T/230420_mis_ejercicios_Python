class DesastreException(Exception):
    pass


def f1():
    raise Exception("Calculo imcompleto", True , 0 [1,3])

try:
    f1()
except Exception as e:
    print(e.args[1])