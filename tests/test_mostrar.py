import unittest
import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

# Test para mostrar productos cuando no hay y cuando hay productos
class TestApp(unittest.TestCase):

    @patch('builtins.input', side_effect=["2", "3"])  # Simulamos la opción de mostrar productos
    def test_mostrar_productos(self, mock_input):
        # Caso 1: No hay productos
        with self.subTest("Sin productos"):
            # Reiniciamos la lista de productos a vacía
            app.productos = []  # Asegúrate de que la lista de productos sea accesible
            app.main()  # Ejecutamos el programa
            self.assertEqual(len(app.productos), 0, "Por defecto no hay productos")

        # Caso 2: Hay productos
        with self.subTest("Con productos"):
            # Agregamos productos de prueba
            app.productos = [
                {"nombre": "Producto 1", "precio": 10.99},
                {"nombre": "Producto 2", "precio": 15.50}
            ]
            app.main()  # Ejecutamos el programa
            self.assertEqual(len(app.productos), 2, "Debe haber 2 productos")

if __name__ == '__main__':
    unittest.main()
