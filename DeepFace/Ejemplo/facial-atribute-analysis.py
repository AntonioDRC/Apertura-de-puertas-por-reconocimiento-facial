from deepface import DeepFace

obj = DeepFace.analyze(img_path = "/home/antoniodrc/GitHub/Apertura-de-puertas-por-reconocimiento-facial/DeepFace/ia-faces/img5.jpeg", 
        actions = ['age', 'gender', 'race', 'emotion']
)
print("Resultado del analisis es: ")
print (obj)
