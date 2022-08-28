FROM nginx:latest as main
ADD main.tar /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:latest as event
ADD event.tar /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:latest as contact
ADD contact.tar /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

FROM node:slim as contactback
ENV NODE_ENV=production
WORKDIR /app
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install --production
COPY . .
CMD [ "node", "server.js" ]