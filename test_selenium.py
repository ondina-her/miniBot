import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL de la aplicación a probar
APP_URL = "http://127.0.0.1:5000"

class MiniJuegoTests(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada prueba."""
        # Selenium 4.6+ gestiona el driver automáticamente
        self.driver = webdriver.Chrome()
        self.driver.get(APP_URL)
        # Espera a que la página y el elemento de puntos estén cargados.
        # Asegúrate de que tu HTML tiene un elemento con id="puntos"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "puntos"))
            )
        except:
            print("\n[ERROR] No se encontró el elemento 'puntos'. HTML visible por Selenium:")
            print(self.driver.page_source)
            raise
        print("\nSetup completado. Página cargada.")

    def tearDown(self):
        """Limpieza después de cada prueba."""
        self.driver.quit()
        print("TearDown completado. Navegador cerrado.")

    def test_movimiento_y_puntuacion(self):
        """
        Prueba el movimiento del jugador y la actualización de la puntuación.
        1. Mover a una casilla verde (0,1) para sumar 5 puntos.
        2. Mover a una casilla roja (0,2) para restar 2 puntos.
        """
        print("Iniciando test_movimiento_y_puntuacion...")
        
        # 1. Obtener puntos iniciales y verificar que son 0
        puntos_iniciales_elem = self.driver.find_element(By.ID, "puntos")
        puntos_iniciales = int(puntos_iniciales_elem.text)
        self.assertEqual(puntos_iniciales, 0, "Los puntos iniciales deberían ser 0")
        print(f"Puntos iniciales: {puntos_iniciales}")

        # 2. Mover a una casilla verde (0,1)
        # El jugador empieza en (0,0). Para llegar a (0,1) debe moverse a la 'derecha'.
        accion_verde = "derecha"
        boton_verde = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[@value='{accion_verde}']"))
        )
        boton_verde.click()
        print(f"Presionado '{accion_verde}' para llegar a casilla verde.")

        # Esperar a que el texto de los puntos se actualice a "5"
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "puntos"), "5")
        )

        # 3. Verificar la nueva puntuación (+5)
        puntos_verdes_elem = self.driver.find_element(By.ID, "puntos")
        puntos_verdes = int(puntos_verdes_elem.text)
        self.assertEqual(puntos_verdes, 5, "La puntuación debería ser 5 tras pisar una casilla verde.")
        print(f"Puntos actuales: {puntos_verdes}. Aserción correcta.")

        # 4. Mover a una casilla roja (0,2)
        # Desde (0,1), nos movemos a la 'derecha' de nuevo para llegar a (0,2)
        accion_roja = "derecha"
        boton_rojo = self.driver.find_element(By.XPATH, f"//button[@value='{accion_roja}']")
        boton_rojo.click()
        print(f"Presionado '{accion_roja}' para llegar a casilla roja.")

        # Esperar a que el texto de los puntos se actualice a "3"
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "puntos"), "3")
        )

        # 5. Verificar la nueva puntuación (-2)
        puntos_rojos_elem = self.driver.find_element(By.ID, "puntos")
        puntos_rojos = int(puntos_rojos_elem.text)
        self.assertEqual(puntos_rojos, 3, "La puntuación debería ser 3 tras pisar una casilla roja.")
        print(f"Puntos finales: {puntos_rojos}. Aserción correcta.")
        

    def test_arriba(self):
        """Prueba el movimiento hacia arriba."""
        print("Iniciando test_arriba...")
        boton_arriba = self.driver.find_element(By.XPATH, "//button[@value='arriba']")
        boton_arriba.click()
        print("Presionado 'arriba'.")
        # Aquí podrías agregar verificaciones adicionales según la lógica del juego.
        time.sleep(1)  # Espera para observar el cambio (opcional)
        print("test_arriba completado.")

    def test_abajo(self):
        """Prueba el movimiento hacia abajo."""
        print("Iniciando test_abajo...")
        boton_abajo = self.driver.find_element(By.XPATH, "//button[@value='abajo']")
        boton_abajo.click()
        print("Presionado 'abajo'.")
        # Aquí podrías agregar verificaciones adicionales según la lógica del juego.
        time.sleep(1)  # Espera para observar el cambio (opcional)
        print("test_abajo completado.")

    def test_izquierda(self):
        """Prueba el movimiento hacia la izquierda."""
        print("Iniciando test_izquierda...")
        boton_izquierda = self.driver.find_element(By.XPATH, "//button[@value='izquierda']")
        boton_izquierda.click()
        print("Presionado 'izquierda'.")
        # Aquí podrías agregar verificaciones adicionales según la lógica del juego.
        time.sleep(1)  # Espera para observar el cambio (opcional)
        print("test_izquierda completado.")
        

if __name__ == '__main__':
    unittest.main()
