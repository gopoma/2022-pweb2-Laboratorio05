# Laboratorio05 Introduction to Django
**¿Qué otros tipos de archivos se deberían agregar a este archivo?**
```
venv
*~
*.swp
*.swo
```
**¿Qué archivos se modificaron al hacer makemigrations y migrate?**

`python manage.py makemigrations`

0001_initial.py was created

`python manage.py migrate`

db.sqlite3 was modified

**¿Qué archivos se modificaron al agregar personas?**

db.sqlite3 was modified

**¿Qué pasa si añadimos un nuevo campo?  los anteriores registros no lo tendrían, entonces ¿Con qué valor se actualizarán?**

Depende del tipo de dato del campo que se actualizó, por ejemplo, en el caso
de las cadenas, se actualizarían con una cadena vacía, en cualquiero otro caso,
se actualizarían con el valor de NULL, a menos que tenga un valor por default,
en ese caso se actualizaría a ese valor.

**¿Cómo crearía un campo que sea obligatorio?**

De acuerdo con las diapositivas sería:

```python
class Persona(models.Model):
    dni = models.CharField(blank=False)
    donador = models.BooleanField(null=False)
```

aunque por defecto se vuelven requeridas...

**¿Cuáles de estos elementos afectarían  a la base de datos? ¿Cuáles no?**

`default = SOME_AWESOME_VALUE && (True := blank = False || null = False)`

Sí, afectaria a la Base de Datos porque al momento querer hacer un cambio
que atente contra la Integridad de la Base de Datos, Django daría alternativas
para que se lleve a cabo al momento de preparar las migraciones y estas alternativas dan valores por default para que se lleve a cabo la operación,
de otra manera, habría que empezar de cero con la Base de Datos.

Los demás casos no aplicarían porque Django directamente no va a dejar que se realizen sin añadir otro factor de Normalización.

**¡Cree más vistas!**

`✘`

**¡CREE SUS PROPIAS PLANTILLAS!**

`✘`

**Revise la documentación sobre el objeto request y pruebe otras de sus propiedades (atributos o métodos)**

`✘`

**Realice sus propias plantillas usando la Base**

`✘`

**Cree más bloques**

`✘`

**Verifique las opciones de navegación que aparecen en el resto de sus vistas**

`✘`

**Revisar el objeto forloop en la documentación oficial y hacer experimentos**

| Variable          | Description   |
|-------------------|-------------  |
|`forloop.counter`    |The current iteration of the loop (1-indexed)|
|`forloop.counter0`   |The current iteration of the loop (0-indexed)|
|`forloop.revcounter` |The number of iterations from the end of the loop (1-indexed)|
|`forloop.revcounter0`|The number of iterations from the end of the loop (0-indexed)|
|`forloop.first`      |True if this is the first time through the loop|
|`forloop.last`       |True if this is the last time through the loop|
|`forloop.parentloop` |For nested loops, this is the loop surrounding the current one|

**Revisar la documentación oficial sobre if, hacer experimentos con otros operadores de comparación**

`if`

* **Boolean operators**
```python
== # {% if myNum == 50 %} {% if myName == "Gustavo" %}
!= # {% if myNum != 100 %}
< # {% if myNum < 16 %}
> # {% if myNum > 25 %}
<= # {% if myNum <= 50 %}
>= # {% if myScore >= 50 %}
in # {% if "Bearer" in "Bearer ..." %}
not in # {% if user not in admins %}
is # {% if user.is_authenticated is True %}
is not # {% if user.is_staff is not False %}
```

* **You are able to use filters in your expressions**
```python
{% if fullname|length >= 100 %}
    <p>Your name is too large!</p>
{% endif %}
```

* **Complex Expressions**
```python
or # {% if isWeekend or isAFreeDay %}
and # {% if myScore >= 50 and myScore <= 75 %}
not # {% if not myScore >= 50 %}
in # {% if user in admins %}
```

**Probar la aplicación de varios otros filtros a variables y bloques, revisando la documentación oficial**

```python
capfirst # Capitalizes the first character of the value. If the first character is not a letter, this filter has no effect.
center # Centers the value in a field of a given width.
cut # Removes all values of arg from the given string.
date # Formats a date according to the given format.
default # If value evaluates to False, uses the given default. Otherwise, uses the value.
length # length
pluralize # Returns a plural suffix if the value is not 1, '1', or an object of length 1. By default, this suffix is 's'.
random # Returns a random item from the given list.
title # Converts a string into titlecase by making words start with an uppercase character and the remaining characters lowercase. This tag makes no effort to keep “trivial words” in lowercase.
```