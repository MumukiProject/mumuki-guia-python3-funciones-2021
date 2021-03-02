¿Y esto con qué se come? Digo, ehm.... ¿cómo se usan estas funciones? ¿Cómo hago para pasarles parámetros y obtener resultados?

Basta con poner el nombre de la función y, entre paréntesis, sus argumentos. ¡Es igual que en Gobstones!

```python
doble(3)
```

Y además podemos usarlas dentro de otras funciones. Por ejemplo:

```python
def doble(numero):
  return 2 * numero

def siguiente_del_doble(numero):
  return doble(numero) + 1
```

O incluso mejor:

```python
def doble(numero):
  return 2 * numero

def siguiente(numero):
  return numero + 1

def siguiente_del_doble(numero):
  return siguiente(doble(numero))
```

> Veamos si se entiende; escribí las siguientes funciones:
>
> * `anterior`: toma un número y devuelve ese número menos uno
> * `triple`: devuelve el triple de un número
> * `anterior_del_triple`, que combina las dos funciones anteriores: multiplica a un número por 3 y le resta 1
>
