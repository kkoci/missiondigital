FROM python:3.11.4

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY Input.json ./

COPY . .

EXPOSE 5000

CMD python app.py

