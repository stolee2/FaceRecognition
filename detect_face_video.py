import cv2

#  Vcituvanje 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Snimanje na Videoto 
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    # Pretvaranje na Siva skala
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detekcija na lice 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Crtanje Kvadrat na sekoe lice
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Ekran
    cv2.imshow('img', img)

    # Pretisni ESC za prekin
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Osloboduvanje na objektot VideoCapture 
cap.release()