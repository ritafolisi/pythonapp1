# img di runtime di python. Migliore img questa

FROM python:alpine      

WORKDIR /app

COPY ./requirements.txt requirements.txt  

RUN pip install -r requirements.txt

COPY app.py . 


COPY templates templates

#far capire a chi legge il file docker che la porta è questa
EXPOSE 5000


CMD ["python", "app.py"]