from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")

    def __str__(self):
        """Retorna str: O nome do curso"""
        return self.name

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
