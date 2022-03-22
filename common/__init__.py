from flask import request
import cv2
import numpy as np
import urllib

def get_image_v1(image='image'):
    if request.files[image]:
        img = cv2.imdecode(np.fromstring(request.files[image].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        if len(img.shape) > 2 and img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img
    return None

def get_image_v2(image='image', url='url'):
    if request.files[image]:
        img = cv2.imdecode(np.fromstring(request.files[image].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        if len(img.shape) > 2 and img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img
    if request.form.get(url):
        req = urllib.urlopen(url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        if len(img.shape) > 2 and img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

    return None