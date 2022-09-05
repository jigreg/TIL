FROM python:3.8.10
WORKDIR /app/
COPY ./* /app/
#RUN pip freeze > requirements.txt
RUN pip install -r /app/requirement.txt
ENV FLASK_APP=app
CMD flask run --host 0.0.0.0 -p 80

