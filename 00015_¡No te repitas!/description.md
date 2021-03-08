Combinar operaciones es muy útil, pero tiene el problema de que ahora tenemos que recordar (o pensar :thought_balloon:) como hacerlo cada vez que lo necesitemos. Esto nos puede llevar a equivocarnos...

```python
# queremos saber si el primero es mas largo que el segundo
ム len("Santiago del Estero") < len("Misiones")
False # Ups ¡era para el otro lado!
```
...o simplemente a aburrirnos por hacer una y otra vez lo mismo :rolling_eyes:. ¿No sería mucho mejor si pudieramos escribir directamente así?:

```python
ム es_mas_largo_que("Santiago del Estero", "Misiones")
```

> :octagonal_sign: ¡Momento! ¿Esto funcionará? Averigualo probándolo en la consola.

