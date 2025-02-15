FROM python:3
WORKDIR /src
COPY Pipfile Pipfile.lock /src/
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    libtiff5-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev
RUN pip install pipenv setuptools wheel
RUN pipenv install --system --deploy --ignore-pipfile
COPY . /src
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]