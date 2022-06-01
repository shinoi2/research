FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive TZ=Asia/Shanghai LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64" CUDA_VISIBLE_DEVICES=0

RUN apt update && \
    apt install -y \
        libopencv-dev \
        libsndfile1 \
        python3-pip \
        wget && \
    apt clean autoclean && \
    apt autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN python3 -m pip install pip --upgrade && \
    pip install flask \
        flask-cors \
        gevent \
        grpcio \
        minio \
        paddle-serving-client==0.8.3 \
        pyopenssl

COPY ./app /root/

ENTRYPOINT cd /root && gunicorn server:app -c /root/gunicorn/gunicorn.conf.py
