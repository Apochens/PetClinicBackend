FROM python:3.11
ENV PYTHONUNBUFFERED 1

WORKDIR /app

#RUN pip3 install --upgrade pip

RUN pip3 install \
        Django==4.1.7 \
        djangorestframework==3.14.0 \
        djangorestframework-simplejwt==5.2.2 \
        PyMySQL==1.0.2 \
        PyYAML==6.0 \
        Pillow==9.4.0 \
        django-cors-headers==3.14.0 \
        -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

EXPOSE 8000

#RUN git clone https://github.com/Apochens/PetClinicBackend.git && \
#    cd PetClinicBackend

#RUN python3 manage.py makemigrations && python3 manage.py migrate
#
## Create superuser
#RUN DJANGO_SUPERUSER_PASSWORD=123456 \
#    DJANGO_SUPERUSER_USERNAME=root \
#    DJANGO_SUPERUSER_EMAIL=123@123.com \
#    python3 manage.py createsuperuser --noinput




