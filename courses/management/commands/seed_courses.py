from django.core.management.base import BaseCommand

from courses.models import Course

class Command(BaseCommand):
    help = "Seed para cadastrar registro na tabela courses"

    def handle(self, *args, **kwargs):
        description = "Curso de python basico"

        courses = [{
            'name': 'Curso de Python Celke ',
            'original_price': 997.43,
            'discounted_price': 847.61,
            'description': description
        },
        {
            'name': 'Curso de Node.js',
            'original_price': 399.43,
            'discounted_price': 198.61,
            'description': description
        },
        {
            'name': 'Curso de Java',
            'original_price': 799.43,
            'discounted_price': 541.61,
            'description': description
        },
        ]

        for course_data in courses:
            Course.objects.update_or_create(
                name=course_data['name'],
                defaults=course_data
            )

            self.stdout.write(self.style.SUCCESS("Cursos adicionado com sucesso!"))
