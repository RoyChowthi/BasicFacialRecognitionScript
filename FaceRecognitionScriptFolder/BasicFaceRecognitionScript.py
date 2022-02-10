import face_recognition

image_of_known_person = face_recognition.load_image_file('known\\BILLGATES.jpg')
face_encoding = face_recognition.face_encodings(image_of_known_person)[0]

unknown_image = face_recognition.load_image_file('unknown\\random_3.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([face_encoding], unknown_face_encoding,tolerance=0.5)

if results[0]:
    print('These are the same people')
else:
    print('These are not the same people')
