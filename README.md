#  Mini Robot Web

“Un minijuego en Flask donde un robot se mueve en un tablero 5x5, sumando o restando puntos según las casillas (verdes +5, rojas -2, neutras 0).”

# Clonar el repositorio
git clone https://github.com/ondina-her/miniBot.git
cd minijuego

# Requisitos previos
- Python 3.9 o superior
- Google Chrome instalado
- ChromeDriver (gestionado automáticamente por Selenium 4.6+)

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py

- Luego abrir en navegador: http://127.0.0.1:5000

# Pruebas automatizadas

Archivo test_selenium.py:

Usa Selenium para simular movimientos del robot.

    - Verifica puntuación al pisar casillas verdes y rojas.

    - Incluye pruebas de límites (arriba/izquierda desde la esquina).

Ejemplo de ejecución:
```
    python test_selenium.py
```

Salida esperada:
```
Ran 4 tests in 26.659s
OK
```

# Estructura del proyecto

```
miniJuego/
│── app.py              # Lógica Flask
│── templates/
│    └── index.html     # Interfaz del juego
│── static/
│    └── style.css      # Estilos
│── test_selenium.py    # Pruebas automatizadas
│── requirements.txt    # Dependencias
```

# Características
- Movimiento del robot con botones ↑ ↓ ← →
- Sistema de puntuación dinámico
- Interfaz web simple y oscura (modo admin pendiente)
- Pruebas automatizadas con Selenium

# Mejoras posibles

- Añadir más tipos de casillas (bonus, obstáculos).
- Mejorar interfaz gráfica.
- Integrar con CI/CD para correr pruebas automáticamente en GitHub Actions.

# Licencia
Este proyecto se distribuye bajo la licencia MIT.

# Autor
Desarrollado por Ondina Hernandez
