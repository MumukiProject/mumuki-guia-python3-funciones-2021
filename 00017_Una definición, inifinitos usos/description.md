Sí, Python nos da operaciones que nos permites resolver diferentes tareas y además nos permite combinarlas, pero el verdadero poder de la programación es que también podemos crear nuestras propias operaciones. 

Y para hacer esto, ¡démosle entonces la bienvenida a _las funciones_! Nuestras nuevas amigas nos permitirán "enseñarle" **una vez** a la computadora a realizar una tarea que originalmente no estaba incluida en el lenguaje mediante una _definición_ como la siguiente... 

```python
def es_mas_largo_que(un_string, otro_string):
  return len(un_string) > len(otro_string)
```

...y luego nos permitá _invocar_ esta función **cuantas veces queramos**: 


```python
ム es_mas_largo_que("Valle de Uco", "Cerro de los Siete Colores")
False
ム es_mas_largo_que("Valle de Uco", "La Punta")
True
```

