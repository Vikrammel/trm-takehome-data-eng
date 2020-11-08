# base img
FROM python:3.8

# set workdir
WORKDIR /app

# copy source files to container
ADD src/ .

# install requirements
RUN pip install -r requirements.txt

# server port
EXPOSE 5000

# run server
ENTRYPOINT ["python", "server.py"]
