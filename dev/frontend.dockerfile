FROM node:13 as builder

RUN mkdir -p /srv/frontend
WORKDIR /srv/frontend

COPY ./frontend/package.json /srv/frontend
COPY ./frontend/package-lock.json /srv/frontend
RUN rm -rf node_modules

RUN apt-get update
RUN npm install
RUN npm install -g @angular/cli

EXPOSE 4200 
CMD ["ng","serve","--host", "0.0.0.0","--port","4200","--disableHostCheck"]
#CMD ["npm", "start", "--host 0.0.0.0", "--port 4200"]
