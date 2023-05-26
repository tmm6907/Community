FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PLACES_API_KEY AIzaSyB1uRbcmzEL5PkkpOZandFVDLch4iyM_UU
WORKDIR /community
ADD . /community
COPY ./requirements.txt /community/requirements.txt
RUN pip install -r requirements.txt
COPY . /community/
EXPOSE 8080 
CMD python3 manage.py runserver 0.0.0.0:8080