FROM: python:3.8.10-buster

# create /app dir >  cd app
WORKDIR /app

# copy requirements.txt from local to docker/app
COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

#copy all files from local  to docker/app
copy . .

expose 5000

CMD ['flask', 'run']
