FROM python:3.9.1
COPY . /python-flask
WORKDIR /python-flask
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "gunicorn", "--workers=1", "--threads=1", "-b 0.0.0.0:5000", "app:app"]