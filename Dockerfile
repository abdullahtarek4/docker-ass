
FROM python:3.8-slim


WORKDIR /app


COPY aaa.py /app/
COPY paragraphs.txt /app/


RUN pip install nltk


CMD ["python", "aaa.py"]
