FROM continuumio/anaconda3

#RUN apt-get update -y && \
#    apt-get install python3.6 -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "project01.py" ]