Sí, Python nos da operaciones que nos permites resolver diferentes tareas y además nos permite combinarlas, pero el verdadero poder de la programación es que también podemos crear nuestras propias operaciones. 

Y para hacer esto, ¡démosle entonces la bienvenida a _las funciones_! :confetti_ball: Nuestras nuevas amigas nos permitirán "enseñarle" **una vez** :one: a la computadora a realizar una tarea que originalmente no estaba incluida en el lenguaje mediante una _definición_ como la siguiente... 

```python
def es_mas_largo_que(un_string, otro_string):
  return len(un_string) > len(otro_string)
```

...y luego podremos _invocar_ a esta función **cuantas veces queramos** :1234:: 

```python
ム es_mas_largo_que("Valle de Uco", "Cerro de los Siete Colores")
False
ム es_mas_largo_que("Valle de Uco", "Cerro de los Siete Colores")
False # las dos veces devuelve lo mismo
```

¡Y no sólo eso! Cada vez que la invoquemos podremos hacerlo con _argumentos_ diferentes :open_mouth: :

```python
ム es_mas_largo_que("Rosario", "Bahía Blanca")
False
ム es_mas_largo_que("Valle de Uco", "La Punta")
True # si los argumentos cambian, el resultado puede ser diferente también 
```

> Veamos si se va entendiendo: 
> 
>  1. Copiá la _definición_ de la función `es_mas_largo_que` en el editor que está debajo
>  2. En la consola, invocá la función `es_mas_largo_que` varias veces con argumentos diferentes. 
>  3. Luego presioná el botón `Enviar`
