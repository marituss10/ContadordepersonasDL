---Instalacion de librerias-----------------
pip install ultralytics
pip install filterpy
pip install PyQt5
pip install opencv-python
pip install torch
pip install numpy
pip install matplotlib

-----Estructura del aprendizaje--------------
1.- Cargar y desplegar el video
2.- Cargar el modelo Yolov5n
3.- Filtrar y obtener bboxes
4.- Validar detecciones
	4.1.- Definir la o las zonas o áreas (polígono)
	4.2.- Validad si la deteccion esta en el polígono
	4.3.- Agregar contador
5.- Visualización

------------Estructura del programa-------
1.- Directorio del video a analizar
2.- Numero de lados para el area1
3.- Numero de lados para el area2
4.- Numero de lados para el area3
5.- Porcentaje de confiabilidad
6.- Seccion de avisos en caso de errores

--------------Consideraciones---------------
- Los datos se deben completar secuencialmente
- En caso de error, en la sección de avisos se notificará el erro existente.
- Cuando se completen todos los parametros, y no se han notificado errores, deben presionar aceptar y esperar unos segundis a que se realice el análisis del video
- Para cerrar el video, deben presiona la tecla "Q", sin activar el Bloq. Mayus.