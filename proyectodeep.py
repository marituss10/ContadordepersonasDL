from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow,QLineEdit
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator, QIntValidator
import cv2
import torch
import numpy as np
from sort import Sort
import matplotlib.path as mplPath
import sys
from tkinter import Tk #Para la ventana de Tkinter
import tkinter.filedialog as tkf #Cuadro de dialogo de Tkinter
from tkinter import filedialog


class Menu1Dialog(QDialog):
	def __init__(self):
		super(Menu1Dialog, self).__init__()
		loadUi('menu.ui', self)  # Cargar la interfaz desde el archivo .ui

		# Puedes realizar configuraciones adicionales aquí, si es necesario
		Dvalidador = QDoubleValidator()
		Ivalidador = QIntValidator()
		self.l_areas1.setValidator(Ivalidador)
		self.l_areas2.setValidator(Ivalidador)
		self.l_areas3.setValidator(Ivalidador)
		self.l_confianza.setValidator(Dvalidador)
		self.b_examinar.clicked.connect(self.directorio)
		self.b_area1.clicked.connect(self.area1)
		self.b_area2.clicked.connect(self.area2)
		self.b_area3.clicked.connect(self.area3)
		self.b_aceptar.clicked.connect(self.aceptar)
		self.b_cancelar.clicked.connect(self.cancelar)

		self.l_areas1.setEnabled(False)
		self.l_areas2.setEnabled(False)
		self.l_areas3.setEnabled(False)
		self.b_area1.setEnabled(False)
		self.b_area2.setEnabled(False)
		self.b_area3.setEnabled(False)
		self.l_confianza.setEnabled(False)

	def directorio(self):
		nombre = filedialog.askopenfilename(initialdir ="/", title = "Seleccione archivo",filetypes = (("Archivos webm","*.webm"), ("Archivos mp4","*.mp4"), ("All files","*.*"))) #muestra el directorio de cada archivo
		self.ruta.setText(nombre)
		ubi = self.ruta.text()
		if ubi == '':
			self.l_avisos.setText("Seleccione un directorio porfavor")
		else:
			self.l_avisos.clear()
			self.b_area1.setEnabled(True)
			self.l_areas1.setEnabled(True)


	def area1(self):
		numero_areas1 = self.l_areas1.text()
		directorio = self.ruta.text()
		if numero_areas1 == '' or directorio == '':
			print("error en area1")
			self.l_avisos.setText("Error en el número de áreas 1")

		else:
			numero_areas1 = int(numero_areas1)
			if numero_areas1 <= 2:
				self.l_avisos.setText("El # de lados del área 1 debe ser mayor que 2")
			else:
				print("area1")
				ubicacion = self.ruta.text()
				lados = int(self.l_areas1.text())
				self.l_areas1.setEnabled(False)
				self.b_area1.setEnabled(False)
				self.b_examinar.setEnabled(False)
				self.l_areas2.setEnabled(True)
				self.b_area2.setEnabled(True)
				self.l_avisos.clear()
				coordinates = []

				def print_coordinates(event, x, y, flags, params):
					if event == cv2.EVENT_LBUTTONDOWN:
						coordinates.append([x, y])
						print(f"Coordenada registrada: [{x}, {y}]")
						self.array1.setText(f"{coordinates}")

				def video(video_path, num_coordinates):
					cap = cv2.VideoCapture(video_path)
					cv2.namedWindow("Frame")
					cv2.setMouseCallback("Frame", print_coordinates)

					while True:
						status, frame = cap.read()

						if not status or len(coordinates) == num_coordinates:
							break

						cv2.imshow("Frame", frame)

						if cv2.waitKey(10) & 0xFF == ord('q'):
							break

					cap.release()
					cv2.destroyAllWindows()

					if len(coordinates) == num_coordinates:
						coordinates_array = np.array(coordinates)
						print(f"Coordenadas guardadas: {coordinates_array}")

				if __name__ == '__main__':
					video(ubicacion, lados)

	def area2(self):
		numero_areas2 = self.l_areas2.text()
		directorio = self.ruta.text()
		if numero_areas2 == '' or directorio == '':
			print("error en area2")
			self.l_avisos.setText("Error en el número de áreas 2")

		else:
			numero_areas2 = int(numero_areas2)
			if numero_areas2 <= 2:
				self.l_avisos.setText("El # de lados del área 2 debe ser mayor que 2")
			else:
				print("area2")
				ubicacion = self.ruta.text()
				lados = int(self.l_areas2.text())
				self.l_areas2.setEnabled(False)
				self.b_area2.setEnabled(False)
				self.l_areas3.setEnabled(True)
				self.b_area3.setEnabled(True)
				self.l_avisos.clear()
				coordinates = []

				def print_coordinates(event, x, y, flags, params):
					if event == cv2.EVENT_LBUTTONDOWN:
						coordinates.append([x, y])
						print(f"Coordenada registrada: [{x}, {y}]")
						self.array2.setText(f"{coordinates}")

				def video(video_path, num_coordinates):
					cap = cv2.VideoCapture(video_path)
					cv2.namedWindow("Frame")
					cv2.setMouseCallback("Frame", print_coordinates)

					while True:
						status, frame = cap.read()

						if not status or len(coordinates) == num_coordinates:
							break

						cv2.imshow("Frame", frame)

						if cv2.waitKey(10) & 0xFF == ord('q'):
							break

					cap.release()
					cv2.destroyAllWindows()

					if len(coordinates) == num_coordinates:
						coordinates_array = np.array(coordinates)
						print(f"Coordenadas guardadas: {coordinates_array}")
						

				if __name__ == '__main__':
					video(ubicacion, lados)

	def area3(self):
		numero_areas3 = self.l_areas3.text()
		directorio = self.ruta.text()
		if numero_areas3 == '' or directorio == '':
			print("error en area3")
			self.l_avisos.setText("Error en el número de áreas 3")

		else:
			numero_areas3 = int(numero_areas3)
			if numero_areas3 <= 2:
				self.l_avisos.setText("El # de lados del área 3 debe ser mayor que 2")
			else:
				print("area3")
				ubicacion = self.ruta.text()
				lados = int(self.l_areas3.text())
				self.l_areas3.setEnabled(False)
				self.b_area3.setEnabled(False)
				self.l_confianza.setEnabled(True)
				self.l_avisos.clear()
				coordinates = []

				def print_coordinates(event, x, y, flags, params):
					if event == cv2.EVENT_LBUTTONDOWN:
						coordinates.append([x, y])
						print(f"Coordenada registrada: [{x}, {y}]")
						self.array3.setText(f"{coordinates}")

				def video(video_path, num_coordinates):
					cap = cv2.VideoCapture(video_path)
					cv2.namedWindow("Frame")
					cv2.setMouseCallback("Frame", print_coordinates)

					while True:
						status, frame = cap.read()

						if not status or len(coordinates) == num_coordinates:
							break

						cv2.imshow("Frame", frame)

						if cv2.waitKey(10) & 0xFF == ord('q'):
							break

					cap.release()
					cv2.destroyAllWindows()

					if len(coordinates) == num_coordinates:
						coordinates_array = np.array(coordinates)
						print(f"Coordenadas guardadas: {coordinates_array}")
						

				if __name__ == '__main__':
					video(ubicacion, lados)

	def aceptar(self):
		
		print("aceptar")
		area1 = self.l_areas1.text()
		area2 = self.l_areas2.text()
		area3 = self.l_areas3.text()
		confianza = self.l_confianza.text()
		ubi = self.ruta.text()
		if (area1 == '' or area2 == '' or area3 == '' or confianza == '' or ubi == ''):
			self.l_avisos.setText("Ingrese todos los datos por favor")
		else:
			self.l_avisos.setText("Presione la letra Q sin MAYUS para cerrar el video")
			directorio = self.ruta.text()
			poligono1 = self.array1.text()
			poligono2 = self.array2.text()
			poligono3 = self.array3.text()

			# Remover los corchetes exteriores y dividir por las comas y espacios
			elementos1 = poligono1[2:-2].split("], [")

			# Convertir cada par de números a una lista y luego a un array
			ZONE1 = np.array([list(map(int, elemento1.split(", "))) for elemento1 in elementos1])

			# Remover los corchetes exteriores y dividir por las comas y espacios
			elementos2 = poligono2[2:-2].split("], [")

			# Convertir cada par de números a una lista y luego a un array
			ZONE2 = np.array([list(map(int, elemento2.split(", "))) for elemento2 in elementos2])

			# Remover los corchetes exteriores y dividir por las comas y espacios
			elementos3 = poligono3[2:-2].split("], [")

			# Convertir cada par de números a una lista y luego a un array
			ZONE3 = np.array([list(map(int, elemento3.split(", "))) for elemento3 in elementos3])

			def get_center(bbox):
				center = ((bbox[0] + bbox[2]) // 2, (bbox[1] + bbox[3]) // 2)
				return center

			def load_model():
				model = torch.hub.load("ultralytics/yolov5", model="yolov5n", pretrained=True)
				return model

			def get_bboxes(preds: object):
				conf = self.l_confianza.text()
				#print(f"{conf}")
				if conf == '':
					print("Ninguna accion")
					df = preds.pandas().xyxy[0]
					df = df[df["confidence"] >= 0.50]
					df = df[df["name"] == "person"]
					return df[["xmin", "ymin", "xmax", "ymax"]].values.astype(int)

				else:
					conf = float(conf)/100
					df = preds.pandas().xyxy[0]
					df = df[df["confidence"] >= conf]
					df = df[df["name"] == "person"]
					return df[["xmin", "ymin", "xmax", "ymax"]].values.astype(int)

			def is_valid_detection(xc, yc, zone):
				return mplPath.Path(zone).contains_point((xc, yc))

			def detector(cap: object):
				model = load_model()

				# Inicializar el tracker SORT
				tracker = Sort()

				while cap.isOpened():
					status, frame = cap.read()
					if not status:
						break

					preds = model(frame)
					bboxes = get_bboxes(preds)

					pred_confidences = preds.xyxy[0][:, 4].cpu().numpy()

					# Aplicar el tracker a las bounding boxes
					trackers = tracker.update(bboxes)

					detections_zone1 = 0
					detections_zone2 = 0
					detections_zone3 = 0

					for i, box in enumerate(trackers):
						xc, yc = get_center(box)
						# Convertir a enteros
						xc, yc = int(xc), int(yc)

						# Dibujar bounding boxes
						cv2.rectangle(img=frame, pt1=(int(box[0]), int(box[1])), pt2=(int(box[2]), int(box[3])), color=(0, 255, 0), thickness=2)

						# Dibujar centro de bounding boxes
						cv2.circle(img=frame, center=(xc, yc), radius=5, color=(255, 0, 0), thickness=-1)

						# Dibujar el ID de la persona
						cv2.putText(img=frame, text=f"id: {int(box[4])}, conf: {pred_confidences[i]:.2f}", org=(int(box[0]), int(box[1])), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 255, 255), thickness=2)

						# Conteo de personas en cada zona
						if is_valid_detection(xc, yc, ZONE1):
							detections_zone1 += 1
						elif is_valid_detection(xc, yc, ZONE2):
							detections_zone2 += 1
						elif is_valid_detection(xc, yc, ZONE3):
							detections_zone3 += 1

					# Mostrar el conteo en pantalla
					cv2.putText(img=frame, text=f"Area 1: {detections_zone1}", org=(50, 400), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 0, 255), thickness=2)
					cv2.putText(img=frame, text=f"Area 2: {detections_zone2}", org=(50, 450), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0), thickness=2)
					cv2.putText(img=frame, text=f"Area 3: {detections_zone3}", org=(50, 500), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 255, 0), thickness=2)

					cv2.polylines(img=frame, pts=[ZONE1], isClosed=True, color=(0, 0, 255), thickness=3)
					cv2.polylines(img=frame, pts=[ZONE2], isClosed=True, color=(255, 0, 0), thickness=3)
					cv2.polylines(img=frame, pts=[ZONE3], isClosed=True, color=(0, 255, 0), thickness=3)

					cv2.imshow("frame", frame)

					if cv2.waitKey(10) & 0xFF == ord('q'):
						break

				cap.release()
				cv2.destroyAllWindows()

			if __name__ == '__main__':
				cap = cv2.VideoCapture(directorio)
				detector(cap)



	def cancelar(self):
		print("cancelar")
		cv2.destroyAllWindows()
		self.ruta.clear()
		self.l_areas1.clear()
		self.l_areas2.clear()
		self.l_areas3.clear()
		self.l_confianza.clear()
		self.l_avisos.clear()
		self.array1.clear()
		self.array2.clear()
		self.array3.clear()
		self.l_confianza.setEnabled(False)
		self.b_examinar.setEnabled(True)
		


if __name__ == '__main__':
	app = QApplication(sys.argv)

	# Crear e inicializar la ventana de diálogo
	menu1_dialog = Menu1Dialog()

	# Mostrar la ventana de diálogo
	menu1_dialog.show()

	sys.exit(app.exec_())