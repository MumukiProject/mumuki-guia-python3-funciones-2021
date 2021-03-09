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

