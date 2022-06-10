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

**Revisar la documentación oficial sobre if, hacer experimentos con otros operadores de comparación**