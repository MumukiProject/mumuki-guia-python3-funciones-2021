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

> ¡A practicar! :muscle: Definí las siguientes funciones:
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
