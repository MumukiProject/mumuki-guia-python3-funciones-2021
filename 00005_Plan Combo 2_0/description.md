¿Y podremos combinar estas funciones al igual que hacíamos con los operadores y funciones que ya venían con Python? ¡Por supuesto! :heart_eyes: En otras palabras, _podemos invocar funciones dentro dentro de definiciones_. Por ejemplo:

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

> Veamos si se entiende; definí las siguientes funciones:
>
> * `anterior`: toma un número y devuelve ese número menos uno
> * `triple`: devuelve el triple de un número
> * `anterior_del_triple`, que combina las dos funciones anteriores: multiplica a un número por 3 y le resta 1
>
