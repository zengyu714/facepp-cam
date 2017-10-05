# Detect faces with OpenCV
```python
face_cascade = cv2.CascadeClassifier("path/to/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 3)

```
# Search faces with facepp

see details in FacePlusPlus/python-sdk [facepp.py](https://github.com/FacePlusPlus/python-sdk/blob/master/python-sdk/facepp.py)
# Play sound with PyGame
```python
import pygame as pg

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)

pg.mixer.music.load(file_name)
pg.mixer.music.play()
```
# Demo
<img src="https://wx3.sinaimg.cn/mw690/9f1c5669ly1fk7if7yrgkg20f40hqb2c.gif" width="335px" alt="blog demo"/>

# Notes
## Ways to load variables/parameters in Python
Solution1

```python
import json
cfg = json.load(open('api_key.json'))
```

Solution2
```python
with open('api_key.config','r') as f:
    for line in f:
        if line:          # skip blank line
            exec(line)
```

Solution3
```python
import pickle
pickle.dump(Face, open('res/saved_face.txt', 'wb'))
Face = pickle.load(open('res/saved_face.txt', 'rb'))

```
