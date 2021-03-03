Combinar funciones es genial, pero tiene el problema de que ahora tenemos que recordar (o pensar) como hacerlo cada vez que lo necesitemos. Esto nos puede llevar a equivocarnos...

```python
# queremos saber si el primero es mas largo que el segundo
ム len("Santiago del Estero") < len("Misiones")
False # Ups ¡era para el otro lado!
```
...o simplemente a aburrirnos :rolling_eyes:. ¿No sería mucho mejor si pudieramos escribir directamente así?:

```python
ム es_mas_largo_que("Santiago del Estero", "Misiones")
True # ¡ahora sí!
```

¡Démosle entonces la bienvenida a _las funciones_! Nuestras nuevas amigas nos permitirán "enseñándole" a la computadora a realizar una tarea que originalmente no estaba incluida en el lenguaje mediante una _definición_ como la siguiente: 

```python
def es_mas_largo_que(un_string, otro_string):
  return len(un_string) > len(otro_string)
```

> Veamos si se entiende

