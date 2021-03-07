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

Como ves 
La definición de funciones debe seguir algunas reglas: 

 1. Debe iniciar con la palabra 




Como vemos, para definir una función