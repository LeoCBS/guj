#change the sources.list

FROM ubuntu:14.04
MAINTAINER likang

#instalando python e scrapy
RUN apt-get update
RUN apt-get install -y python python-pip python-dev libxml2-dev libxslt-dev libffi-dev libssl-dev 
RUN pip install lxml && pip install pyopenssl && pip install Scrapy && pip install service_identity

#instalando o git
RUN apt-get install -y git

#criando uma pasta para o projeto scrapy
RUN mkdir /scrapyguj

#clonando projeto
RUN cd /scrapyguj; git clone https://github.com/LeoCBS/guj.git

#rodando scrapy
WORKDIR /scrapyguj/guj
CMD ["scrapy", "crawl", "java", "-o items.json"]





