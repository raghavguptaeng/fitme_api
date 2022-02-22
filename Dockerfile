FROM python:3
RUN pip3 install falcon gunicorn
ADD . /code
WORKDIR /code
CMD gunicorn -b 0.0.0.0:80 fitme:api