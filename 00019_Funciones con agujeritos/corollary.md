¡Exactamente! Todas las opciones son correctas. :ok_hand:

Una función puede _declarar_ tantos parámetros como necesite en su definición; por cada uno de ellos, deberemos pasar un argumento al invocarla. Lo interesante es que no importa qué argumentos utilicemos, ya que a cada uno lo conoceremos con el nombre de su parámetro. En este ejemplo, si escribimos en la consola...

```python
ム suma_longitudes("aprendiendo", "programación")
```
...dentro de la función `suma_longitudes` el argumento `"aprendiendo"` será `un_string` y `"programación"` será `otro_string`:

```python
def suma_longitudes(un_string, otro_string):
  #                     ˆ           ˆ
  #                     |           |
  #              "aprendiendo"  "programación"
  return len(un_string) + len(otro_string)  
  #            ˆ                  ˆ
  #            |                  |
  #     len("aprendiendo")  len("programación")
```

Sin embargo, si lo invocamos escribiendo...

```python
ム suma_longitudes("conociendo", "Python")
```

... ahora el parámetro `un_string` tiene como valor `"conociendo"` y `un_string` _vale_ `"Python"`.

¡Por eso es tan importante darle un buen nombre! 