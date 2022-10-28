from deepface import DeepFace

print("Buscando rostro")

df = DeepFace.find(img_path = "/home/antoniodrc/GitHub/Apertura-de-puertas-por-reconocimiento-facial/DeepFace/ia-faces/img8.jpg" , db_path = "/home/antoniodrc/GitHub/Apertura-de-puertas-por-reconocimiento-facial/DeepFace/my_db")

print("Resultado ")
print(df)
print("Seleccion")
print(df[0])
