"""
Las funciones lambda sirven para crear funciones anónimas (función sin nombre) y sobre la marcha
La función lambda no se puede utilizar si tiene bucles, condicionales..., solo para funciones simples
Tambien se le puede llamar funciones on the go, on demand, online
"""

def area_triangulo1 (base, altura):
    return (base*altura)/2
triangulo1=area_triangulo1(5,8)
print(triangulo1)

#FUNCIÓN LAMBDA
area_triangulo2 = lambda base,altura:(base*altura)/2 #variable = lambda parametros : lo que devuelve
triangulo2=area_triangulo2(5,8)
print(triangulo2)