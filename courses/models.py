from django.db import models
import os

class Course(models.Model):
    """Modelo que representa um curso"""
    name = models.CharField(max_length=255, verbose_name="Nome")
    original_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço Original",
        blank=True,
        null=True)

    discounted_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Preço Desconto",
        blank=True,
        null=True)

    image = models.ImageField(
        upload_to="courses/", 
        verbose_name="Imagem",
        blank=True,
        null=True)

    description = models.TextField(verbose_name="Descrição", blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")

    #Sobrescrever o Método save no modelo
    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Course.objects.get(pk=self.pk).image

            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)

        super().delete(*args, **kwargs)

    def __str__(self):
        """Retorna str: O nome do curso"""
        return self.name

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
