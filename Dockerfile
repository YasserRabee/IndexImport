## requires statically linked go binary to be compiled
## to ./magalix/simple-service before docker build
#FROM golang:latest
## executable folder
#RUN mkdir /magalix
#COPY simple-service /magalix
## run micro-service after boot up
#ENTRYPOINT ["/magalix/simple-service"]
##expose port 8080
#EXPOSE 8080


FROM python:3

WORKDIR /usr/src/app/src/data

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./OpenWeatherMap.py", "98103" ]