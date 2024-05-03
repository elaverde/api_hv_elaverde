FROM python:3.8.5-alpine

# Instalar las dependencias necesarias para wkhtmltopdf
RUN apk update && apk add --no-cache gcc g++ make\
    libstdc++ \
    libx11 glib libxrender libxext libintl \
    ttf-dejavu \
    ttf-droid \
    ttf-freefont \
    ttf-liberation \
    pkgconfig \
    mariadb-dev \
    git \
    ttf-ubuntu-font-family

# Copiar wkhtmltopdf desde una imagen que ya lo tiene instalado
COPY --from=surnet/alpine-wkhtmltopdf:3.16.2-0.12.6-full /bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf
COPY --from=surnet/alpine-wkhtmltopdf:3.16.2-0.12.6-full /bin/libwkhtmltox.so /usr/local/lib/libwkhtmltox.so

# Copiar el directorio actual al contenedor
COPY ./ /app

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias especificadas en requirements.txt
RUN pip3 install -r requirements.txt

RUN ls -a
RUN pip3 install -r requirements.txt
CMD [ "gunicorn", "--bind", "0.0.0.0:5000","--reload", "wsgi:app" ]
