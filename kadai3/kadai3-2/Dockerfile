FROM python:3.6.8-alpine
COPY ./requirements.txt /var/app/requirements.txt
WORKDIR /var/app
RUN pip install -r requirements.txt
ENV FLASK_ENV=development
CMD  ["flask", "run", "--host=0.0.0.0", "--port=5000"]