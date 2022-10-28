from deepface import DeepFace
print("Se ha comparado dos imagenes. Se verificara que la persona sea la misma")
print("Cargando...")

#Cuando se utilice una imagen se tiene que cambiar la ruta de cada imagen de la que se vaya a utilizar, asi como el nombre y el tipo de archivo
result = DeepFace.verify(img1_path = "/home/antoniodrc/GitHub/Apertura-de-puertas-por-reconocimiento-facial/DeepFace/ia-faces/img2.jpg" , img2_path = "/home/antoniodrc/GitHub/Apertura-de-puertas-por-reconocimiento-facial/DeepFace/ia-faces/img3.jpeg")

print("Resultados")
print (result)