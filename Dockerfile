FROM python:3.8.10-buster

# create /app dir >  cd app
WORKDIR /app

# copy requirements.txt from local to docker/app
COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt
# RUN APT-GET install ...

#copy all files from local  to docker/app
copy . .

expose 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

