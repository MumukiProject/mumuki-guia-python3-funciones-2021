Muchas veces queremos escribir programas que trabajen con texto :page_facing_up:: queremos saber cuántas palabras hay en un libro, o convertir minúsculas a mayúsculas, o saber en qué parte de un texto está otro.

Para este tipo de problemas tenemos los _strings_, también llamados _cadenas de caracteres_:

* `"Ahora la bebé tiene que dormir en la cuna"`
* `'El hierro nos ayuda a jugar'`
* `"¡Hola Miguel!"`

Como se observa, todos los strings están encerrados entre comillas simples o dobles. ¡Da igual usar unas u otras! Pero sé consistente: por ejemplo, si abriste comilla doble, tenés que cerrar comilla doble. Además, un string puede estar formado por (casi) cualquier carácter: letras, números, símbolos, espacios, etc.

¿Y qué podemos hacer con los strings? Por ejemplo, compararlos, como a cualquier otro valor:

```python
ム "hola" == "Hola"
False

ム "todo el mundo" == "todo el mundo"
True
```

> Veamos si queda claro: escribí la función `es_fin_de_semana` que tome un string que represente el nombre de un día de la semana, y nos diga si es `"sábado"` o `"domingo"`:
>
> ```python
> ム es_fin_de_semana("sábado")
> True
> ム es_fin_de_semana("martes")
> False
> ```

