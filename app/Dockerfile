FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install flask mysql-connector-python
EXPOSE 8080
CMD ["python", "app.py"]
