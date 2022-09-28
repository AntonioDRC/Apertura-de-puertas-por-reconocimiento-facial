from deepface import DeepFace
obj = DeepFace.analyze(img_path = "/home/antoniodrc/Downloads/face(2).jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)
print ("El resultado es: ")
print(obj)