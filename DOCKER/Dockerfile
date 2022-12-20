FROM python:3.7.3

ADD Exc.py /

COPY test1.csv ./

COPY ml.pkl ./

COPY Exc.py ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python","./Exc.py"]