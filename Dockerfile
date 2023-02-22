FROM python:3.8

ADD main.py .

RUN pip install pyzmq

CMD ["python", "./main.py"]

