FROM python:3.11
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install \
        Django==4.1.7 \
        djangorestframework==3.14.0 \
        djangorestframework-simplejwt==5.2.2 \
        PyMySQL==1.0.2 \
        PyYAML==6.0 \
        Pillow==9.4.0 \
        django-cors-headers==3.14.0 \
        -i https://mirrors.aliyun.com/pypi/simple

COPY . .

RUN sed -i "s/'127.0.0.1'/'mariadb'/g" ./PetClinicBackend/settings.py



