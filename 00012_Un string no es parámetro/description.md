Como vimos, las funciones pueden tener uno o más parámetros, y además los string pueden ser pasados como argumentos. ¿Deberíamos tener alguna consideración especial?

¿Y qué podemos hacer con los strings, además de compararlos? ¡Varias cosas! Por ejemplo, podemos preguntarles cuál es su cantidad de letras:

```python
ム len("biblioteca")
10
ム len("babel")
5
```

O también podemos _concatenarlos_, es decir, obtener **uno nuevo** que junta dos strings:

```python
ム "aa" + "bb"
"aabb"
ム "sus anaqueles " + "registran todas las combinaciones"
"sus anaqueles registran todas las combinaciones"
```

Por otro lado, la sintaxis de algunas funciones de `string`s es _apenitas_ diferente de lo que venimos haciendo: hay que prefijarlas con `str.`. Por ejemplo, la función que devuelve si un `string` comienza con otro es `str.startswith`:

```python
ム str.startswith("una página", "una")
True
ム str.startswith("la biblioteca", "todos los fuegos")
False
```

> Veamos si queda claro: escribí una función `longitud_nombre_completo`, que tome un nombre y un apellido, y devuelva su longitud total, **contando un espacio extra** para separar a ambos:
>
>```python
> ム longitud_nombre_completo("Cosme", "Fulanito")
>14
>```
