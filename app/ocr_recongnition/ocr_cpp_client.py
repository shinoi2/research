# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: disable=doc-string-missing

import base64
import codecs
import os
import sys
import time

import cv2
import numpy as np
from ocr_reader import OCRReader
from paddle_serving_app.reader import (Div, Normalize, ResizeByFactor,
                                       Sequential, Transpose, URL2Image)
from paddle_serving_client import Client

client = Client()
# TODO:load_client need to load more than one client model.
# this need to figure out some details.
client.load_client_config(sys.argv[1:])
client.connect(["127.0.0.1:8181"])

import paddle

ocr_reader = OCRReader(char_dict_path="./ppocr_keys_v1.txt")


def cv2_to_base64(image):
    return base64.b64encode(image).decode(
        'utf8')  #data.tostring()).decode('utf8')


def _check_image_file(path):
    img_end = {'jpg', 'bmp', 'png', 'jpeg', 'rgb', 'tif', 'tiff', 'gif'}
    return any([path.lower().endswith(e) for e in img_end])

for img_file in ["/home/pji/test1.jpg", "/home/pji/test2.jpg"]:
    start_time = time.time()
    with open(img_file, 'rb') as file:
        image_data = file.read()
    image = cv2_to_base64(image_data)
    res_list = []
    fetch_map = client.predict(feed={"x": image}, fetch=[], batch=True)
    if fetch_map is None:
        print('no results')
    else:
        if "text" in fetch_map:
            print(fetch_map)
            for x in fetch_map["text"]:
                x = codecs.encode(x)
                words = base64.b64decode(x).decode('utf-8')
                res_list.append(words)
        else:
            try:
                one_batch_res = ocr_reader.postprocess(
                    fetch_map, with_score=True)
                print(one_batch_res)
                for res in one_batch_res:
                    res_list.append(res[0])
            except:
                print('no results')
        res = {"res": str(res_list)}
        print(res)
    print(time.time() - start_time)
