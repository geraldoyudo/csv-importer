FROM python:alpine3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./import-csv.py
CMD [ "python", "./import-csv.py", "sample.csv" ]