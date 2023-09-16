FROM python:3.9

WORKDIR /mediaplex

ADD requirements.txt requirements.txt

ADD main.py main.py

RUN pip install -r requirements.txt

ADD mediaplex mediaplex

EXPOSE 8080

CMD ["python","main.py"]


