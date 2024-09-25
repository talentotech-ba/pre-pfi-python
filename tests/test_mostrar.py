
import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch
# Test para mostrar productos cuando no hay productos
@patch('builtins.input', side_effect=["2", "3"])  # Simulamos la opción de mostrar productos
def test_mostrar_productos_sin_productos(mock_input):
    app.productos = []  # Aseguramos que la lista esté vacía
    app.main()  # Ejecutamos el programa
    assert len(app.productos) == 0  # Verificamos que la lista sigue vacía

# Test para la opción de salir
@patch('builtins.input', side_effect=["3"])  # Simulamos la opción de salida
def test_salir(mock_input):
    app.main()  # Ejecutamos el programa
    assert True  # Verificamos que el programa termina sin errores
