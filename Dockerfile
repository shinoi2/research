FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive TZ=Asia/Shanghai LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64" CUDA_VISIBLE_DEVICES=0

RUN apt update && \
    apt install -y \
        libopencv-dev \
        libsndfile1 \
        python3-opencv \
        python3-pip \
        wget && \
    apt clean autoclean && \
    apt autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN wget https://paddle-serving.bj.bcebos.com/others/centos_ssl.tar && \
    tar xf centos_ssl.tar && rm -rf centos_ssl.tar && \
    mv libcrypto.so.1.0.2k /usr/lib/libcrypto.so.1.0.2k && mv libssl.so.1.0.2k /usr/lib/libssl.so.1.0.2k && \
    ln -sf /usr/lib/libcrypto.so.1.0.2k /usr/lib/libcrypto.so.10 && \
    ln -sf /usr/lib/libssl.so.1.0.2k /usr/lib/libssl.so.10 && \
    ln -sf /usr/lib/libcrypto.so.10 /usr/lib/libcrypto.so && \
    ln -sf /usr/lib/libssl.so.10 /usr/lib/libssl.so

RUN python3 -m pip install pip --upgrade && \
    pip install flask \
        flask-cors \
        gunicorn \
        gevent \
        grpcio \
        minio \
        paddle-serving-app==0.8.3 \
        paddle-serving-client==0.8.3 \
        pyopenssl \
        soundfile

COPY ./app /root/

ENTRYPOINT cd /root && gunicorn server:app -c /root/gunicorn/gunicorn.conf.py
