import unittest
import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

# Test para mostrar productos cuando no hay productos
class TestApp(unittest.TestCase):
        
    @patch('builtins.input', side_effect=["2", "3"])  # Simulamos la opción de mostrar productos
    def test_mostrar_productos_sin_productos(self, mock_input):
        app.main()  # Ejecutamos el programa
        
        with self.subTest("Verificando cantidad de productos"):
            self.assertEqual(len(app.productos), 0, "Por defecto no hay productos" )

if __name__ == '__main__':
    unittest.main()
