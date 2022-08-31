FROM nginx:latest AS main
ADD main.tar /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:latest AS event
ADD event.tar /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:latest AS contact
ADD contact.tar /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

FROM node:10.24.1 AS node
RUN mkdir -p /app
WORKDIR /app
COPY ./node/package*.json /app/
RUN npm install
COPY ./node/index.js /app/
EXPOSE 4000
CMD [ "node", "index.js" ]
