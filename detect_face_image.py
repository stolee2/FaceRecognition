import cv2

# Vcituvanje 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Citanje na Vlezna slika 
img = cv2.imread('test.jpg')

# Konvertiranje vo sivi tonovi
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# citanje lice
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Crtanje na Kvadrat na liceto 
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
