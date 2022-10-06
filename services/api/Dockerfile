FROM python:3.9

# RUN pip install fastapi uvicorn spacy
# RUN pip install -r requirements.txt

COPY . /api/api
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

ENV PYTHONPATH=/api
WORKDIR /api

# RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]