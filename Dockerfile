FROM python:3.8.5-alpine
COPY ./ /app/
WORKDIR /app
RUN apk update && \
    apk add --no-cache gcc g++ make
RUN apk add pkgconfig
RUN apk add mariadb-dev





RUN ls -a
RUN pip3 install -r requirements.txt
CMD [ "gunicorn", "--bind", "0.0.0.0:5000","--reload", "wsgi:app" ]
