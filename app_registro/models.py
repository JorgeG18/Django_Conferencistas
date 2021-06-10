from django.db import models

# Create your models here.
'''
    CharField(max_length=50)
    TextField()
    IntergerField()
    DecimalField(max_digits=10, decimal_places=2)
    PositiveIntegerField()
    SmallIntegerField()
    BooleanFiel(default=True or False)
    EmailField()
    ImageField(upload_to='fotos)
    FieldFieldupload_to='archivos')
    SlugFieldd()

    Campos para establecer relaciones entre modelos:

    ForeignKey()
    OneToOneFiel()
    ManyToManyField()
'''

class Conferencista(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField( max_length=50)
    experiencia = models.TextField()
    
    def __str__(self):
        return self.nombre


class Conferencias(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField()
    hora = models.TimeField()
    conferencista = models.ForeignKey(Conferencista, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Conferencia; {self.nombre} - Conferencista: {self.conferencista}'

class Participantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    twitter = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    