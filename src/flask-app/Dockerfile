# Use an official Python runtime as an image
FROM python:3.6.5

EXPOSE 5000
# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

CMD ["python","main.py"]
