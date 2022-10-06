FROM python:3.9.7-slim

# RUN pip install fastapi uvicorn
# COPY requirements.txt /tmp
# RUN pip install -r requirements.txt

COPY . /api/api

ENV PYTHONPATH=/api
WORKDIR /api

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]