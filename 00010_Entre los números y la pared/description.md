¡Hagamos un breve repaso de los booleanos antes de continuar!

* Se puede hacer la conjunción lógica entre dos booleanos (_y lógico_), mediante el operador `and`. Por ejemplo: `esta_lloviendo and hace_calor`
* Se puede hacer la disyunción lógica entre dos booleanos (_o lógico_), mediante el operador `or` haciendo `es_verano or es_primavera`

Y además de estos dos operadores, contamos con un tercero: el operador de negación `not`, que convierte al `True` en `False` y viceversa:

```python
ム not True
False
ム not False
True
```

Al igual que los otros operadores que fuimos aprendiendo, el `not` sirve para negar cualquier tipo de expresión booleana, incluso el resultado de una función: 

```python
# si tenemos una función que nos dice si algo es de un color...
ムes_de_color("cielo", "verde")
False
# ...podemos negar su resultado usando not
ムnot es_de_color("cielo", "verde")
True
```

> ¡A practicar! :muscle: Definí las siguientes funciones:
>
> * `esta_entre`, que tome tres números y diga si el primero es mayor o igual al segundo y menor o igual al tercero.
> * `esta_fuera_de_rango`: que tome tres números y haga exactamente lo contrario de `esta_entre`. En otras palabras, debe decir si el primero es menor al segundo o mayor al tercero.
>
> ```python
> ムesta_entre(3, 1, 10)
> True
> ムesta_entre(90, 1, 10)
> False
> ムesta_fuera_de_rango(10, 1, 10)
> False
> ムesta_fuera_de_rango(17, 1, 10)
> True
> ```
>
