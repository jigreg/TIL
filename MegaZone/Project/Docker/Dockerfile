FROM nginx:latest AS main
ADD main.tar /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

FROM nginx:latest AS event
ADD event.tar /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]

FROM python:3.8.10 AS contact
WORKDIR /app/
COPY ./contact/* /app/
#RUN pip freeze > requirements.txt
RUN pip install -r /app/requirement.txt
ENV FLASK_APP=app
CMD flask run --host 0.0.0.0 -p 80