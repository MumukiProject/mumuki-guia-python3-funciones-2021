¡Hagamos un breve repaso de los booleanos antes de continuar!

* Se pueden negar, mediante el operador `not`. Por ejemplo: `not hay_comida`
* Se puede hacer la conjunción lógica entre dos booleanos (_y lógico_), mediante el operador `and`. Por ejemplo: `hay_comida and hay_bebida`
* Se puede hacer la disyunción lógica entre dos booleanos (_o lógico_), mediante el operador `or` haciendo `una_expresion or otra_expresion`

> Escribí las siguientes funciones:
>
> * `esta_entre`, que tome tres números y diga si el primero es mayor al segundo y menor al tercero.
> * `esta_fuera_de_rango`: que tome tres números y diga si el primero es menor al segundo o mayor al tercero
>
> ```python
> ム esta_entre(3, 1, 10)
> True
> ム esta_entre(90, 1, 10)
> False
> ム esta_entre(10, 1, 10)
> False
> ム esta_fuera_de_rango(17, 1, 10)
> True
> ```
>
