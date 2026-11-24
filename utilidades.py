def precio_final(precio, descuento=0):
    resultado = (precio * (1 - descuento/100)) * 1.19
    return resultado