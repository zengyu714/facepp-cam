# coding: utf-8
# ref: https://github.com/FacePlusPlus/python-sdk/blob/master/python-sdk/call.py

from utils.facepp import API, File
import utils
import cv2

api = utils.init()

# # create a Faceset to save FaceToken
# -----------------------------------
# ret = api.faceset.create(outer_id='test')
# print_result("faceset create", ret)
#
# # detect image
# Face = {}
#
# namelist = ['key1','key2','key3']
# for name in namelist:
#     img_dir = 'res/' + name + '.jpg'
#     res = api.detect(image_file = File(img_dir))
#     # print_result(name, res)
#     Face[name] = res["faces"][0]["face_token"]

# # save vairable Face in ROM
# ---------------------------
# import pickle
# pickle.dump(Face, open('res/saved_face.txt', 'wb'))

# # save FaceToken into Faceset
# -----------------------------
# api.faceset.addface(outer_id = 'test',face_tokens = Face.itervalues())

# # delete a Faceset, if need
# ---------------------------
# api.faceset.delete(outer_id = 'test',check_empty = 0)


import pickle
Face = pickle.load(open('res/saved_face.txt', 'rb'))

face_cascade = cv2.CascadeClassifier("path/to/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(1)  # default is 0, here is a USB camera

while cap.isOpened():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x,y,w,h) in faces:
        # print 'x: %d,y: %d,w: %d,h: %d' %(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('Face detecting...',img)

    # keyboard inputs
    ch = cv2.waitKey(1)
    if ch == 27:
        break

    if len(faces) and ch == ord('p'): # detect faces, named after 'photo'
        face_specified = img[y:y+h,x:x+w]
        face_search_dir = 'res/temp.jpg'
        cv2.imwrite(face_search_dir,face_specified)

        # detect image and search in faceset
        # get the face_token
        ret = api.detect(image_file = File(face_search_dir))
        # print_result("detect", ret)
        search_result = api.search(face_token = ret["faces"][0]["face_token"], outer_id = 'test')
        # print_result('search', search_result)
        if search_result['results'][0]['confidence'] > 65:   # actually in the face set
            print '=' * 60
            for k, v in Face.iteritems():
                if v == search_result['results'][0]['face_token']:
                    print 'The person with highest confidence:', k
                    utils.play_music('res/' + k + '.mp3')
                    break
        else:
            utils.play_music('res/unknown.mp3')

cap.release()
cv2.destroyAllWindows()
