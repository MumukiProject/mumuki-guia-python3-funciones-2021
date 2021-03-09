Como vimos, un string puede ser pasado como argumento a una función...

```python
ム es_biblioteca("Biblioteca De Babel")
True
ム es_biblioteca("Biblioteca Del Congreso")
True
ム es_biblioteca("Teatro Colón")
False
```

...y además, las funciones pueden tener parámetros, uno por cada argumentos que necesite recibir. ¿Deberíamos tener entonces alguna consideración especial cuando combinamos estas dos ideas? Por ejemplo, ¿está bien este código?:

```python
def es_biblioteca("lugar")
  return "biblioteca" in "lugar"
```

Por ejemplo, si tenemos 


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
