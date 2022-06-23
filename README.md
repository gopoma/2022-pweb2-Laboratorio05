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

**Complete la descripción del modelo de persona**

**Intente llenar el formulario para hacerlo inválido**

**Pruebe qué ocurre si no incluímos el campo “donador” en el formulario**

`¿De qué se trata este error?`

```sql
IntegrityError at /agregar/
NOT NULL constraint failed: personas_persona.donador
```

El campo `donador` no puede ser nulo, y cuando no incluimos el campo `donador` en el formulario, entonces este campo se rellena con un valor nulo, lo que ocasiona este error de Integridad en la Base de Datos

`¿Cómo se puede solucionar?`

En primera instancia, podemos recolocar el campo `donador` en el formulario. En segunda instancia, podemos hacer que el campo `donador` sea nullable en el modelo de Persona. En tercera instancia, podemos hacer que el campo `donador` acepte un valor por default.

**Note que una de nuestras vistas se invoca con GET y luego con POST**

Sí, `personaCreateView`

**¿En qué momento se hace llamada GET y en qué momento se hace la llamada POST?**

Cuando colocamos el URL `/personas/create` en el Navegador (Cliente) y damos Enter, entonces ahí se realiza una petición del tipo `GET`, solicitando un archivo HTML, en ese mismo archivo tenemos un formulario, que cuando lo llenamos y lo enviamos, ahí estamos haciendo una petición del tipo `POST`.

**¿El formulario tiene los mismos campos y tipos que el modelo?**

El formulario **sí** tiene los mismos tipos que el modelo, aunque teniendo en cuenta que un campo viene acompañado de sus restricciones, podemos decir que **no** porque no hemos definido una restricción para el número de caracteres máximo y puede ser un punto de debilidad puesto a que por ahí pueden detornarnos un Error de Integridad en la Base de Datos.

**Revise si algún tipo de dato permitido en el modelo no existe en los tipos de datos de forms**

**Sí**, existen tipos de dato permitidos en el modelo que no existen en los tipos de datos de forms, como:

* `BinaryField`
* `BigIntegerField`
* `CommaSeparatedIntegerField`

**Inspeccione el código HTML generado, observe los tags generados**

`done c:`

**Modifique el template y Explore otras opciones distintas a form.as_p**

`done c:`

**Ponga a prueba la seguridad de Django haciendo algo de hacking sobre el código HTML: haga que los campos no sean “requeridos”**

`done c:`