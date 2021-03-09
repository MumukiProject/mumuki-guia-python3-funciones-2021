Como vimos, un string puede ser pasado como argumento a una función...

```python
ム es_biblioteca("Biblioteca De Babel")
True
ム es_biblioteca("Biblioteca Del Congreso")
True
ム es_biblioteca("Teatro Colón")
False
```

...y además, las funciones pueden tener parámetros, uno por cada argumento que necesite recibir. 

> ¡Momento! ¿Tendremos que escribir de forma diferente nuestros parámetros cuando _son de tipo_ string? :thinking:
>
> Por ejemplo, observá la siguiente definición es `es_biblioteca`...
> 
> ```python
> def es_biblioteca("lugar")
>  return "biblioteca" in "lugar"
> ```
> ...¿está bien escrita?

