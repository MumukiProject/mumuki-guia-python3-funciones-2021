Probablemente habrás notado que las funciones que definimos hasta ahora podían devolver tanto números como booleanos. Es más: **pueden devolver cualquier tipo de dato** :exploding_head:. Pero, ¿qué hay de lo que _entra_ a la función? ¿Cuántos argumentos podemos pasarles? ¿Y qué son exactamente los parámetros? 

La respuesta que los parámetros son _...redoble de tambores :drum:..._  ¡pequeños agujeros! :face_with_raised_eyebrow: 

Por ejemplo, en esta definición estamos _declarando_ **un** parámetro llamado `un_numero`... 

```python
def mitad(un_numero): # un_numero es un parámetro
  return un_numero / 2  
```

...que sirve para que `mitad` pueda recibir exactamente **un** argumento: 

```python
ム mitad(4) # 4 es un argumento
2
```

Por ejemplo, cuando invocamos `mitad` con el argumento `4`, a través de este "agujerito" llamado `un_numero` le llegará el valor `4`, que luego nuestra función podrá dividir por dos y retornar su resultado. En cambio, si la invocamos así...


```python
ム mitad(10) # 10 es otro argumento
5
```

...a través del parámetro `un_numero` llegará a `mitad` el `10` con el que invocamos la función. Y nuevamente, lo dividirá por dos y retornará el `5`.    




