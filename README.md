# ContadordepersonasDL
Programa de Deep Learning que realiza el conteo de personas que ingresan a un área determinada en tiempo real.
# Interfaz Principal

![deep](https://github.com/marituss10/ContadordepersonasDL/assets/150117562/3a706f49-6c0a-449b-b644-aeb1c2b45eb4)

# Instalacion de librerias

pip install ultralytics

pip install filterpy

pip install PyQt5

pip install opencv-python

pip install torch

pip install numpy

pip install matplotlib


# Estructura del aprendizaje

1.- Cargar y desplegar el video

2.- Cargar el modelo Yolov5n

3.- Filtrar y obtener bboxes

4.- Validar detecciones

	4.1.- Definir la o las zonas o áreas (polígono)

 	4.2.- Validad si la deteccion esta en el polígono

	4.3.- Agregar contador

5.- Visualización

# Estructura del programa

1.- Directorio del video a analizar

2.- Numero de lados para el area1

3.- Numero de lados para el area2

4.- Numero de lados para el area3

5.- Porcentaje de confiabilidad

6.- Seccion de avisos en caso de errores

# Consideraciones

- Los datos se deben completar secuencialmente

- En caso de error, en la sección de avisos se notificará el erro existente.

- Cuando se completen todos los parametros, y no se han notificado errores, deben presionar aceptar y esperar unos segundis a que se realice el análisis del video

- Para cerrar el video, deben presiona la tecla "Q", sin activar el Bloq. Mayus.

- El archivo principal del programa lleva de nombre "proyectodeep.py"

# Funcionamiento

![FUNCIONAMIENTO](https://github.com/marituss10/ContadordepersonasDL/assets/150117562/cbd691c5-2cfe-46a0-acc1-a92aa24d20e5)
![FUNCIONAMIENTO2](https://github.com/marituss10/ContadordepersonasDL/assets/150117562/d3a2e474-920f-4081-a843-07f006a1e383)

