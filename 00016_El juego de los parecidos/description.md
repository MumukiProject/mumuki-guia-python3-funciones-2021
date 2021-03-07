Veamos ahora la definición de otra función... 

```python
def es_pregunta(oracion):
  return str.startswith(oracion, "¿") and str.endswith(oracion, "?") 
```
...la cual podemos usar así: 

```python
ム es_pregunta("¿Qué hora es?")
True
```

¿Se parece la definición de esta función a la anterior? ¿Por qué será?

> :mag: Compará esta nueva definición con la que vimos anteriormente...
>
> ```python
> def es_mas_largo_que(un_string, otro_string):
>   return len(un_string) > len(otro_string)
> ```
>
> ...y respondé qué tienen en común.
