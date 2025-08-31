from django.test import TestCase
from django.urls import reverse
from .models import Estudiante


class EstudianteModelTest(TestCase):
    def test_creacion_estudiante(self):
     e = Estudiante.objects.create(
        nombre="Ana Perez", carrera="Sistemas", ciclo=3, correo="ana@example.com"
)
     self.assertEqual(str(e), "Ana Perez (Sistemas)")


class EstudianteViewsTest(TestCase):
    def setUp(self):
        self.e = Estudiante.objects.create(
    nombre="Luis", carrera="Industrial", ciclo=2, correo="luis@example.com"
)


    def test_lista_status(self):
        url = reverse("estudiantes:lista")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Control de Estudiantes")


def test_crear(self):
    url = reverse("estudiantes:crear")
    data = {"nombre": "Mia", "carrera": "Sistemas", "ciclo": 1, "correo": "mia@example.com"}
    resp = self.client.post(url, data, follow=True)
    self.assertEqual(resp.status_code, 200)
    self.assertTrue(Estudiante.objects.filter(correo="mia@example.com").exists())