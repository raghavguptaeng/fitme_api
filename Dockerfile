FROM python:3
RUN pip3 install falcon
RUN pip3 install gunicorn
CMD gunicorn -b 0.0.0.0:8000 app