
FROM python:2.7
COPY . /app
WORKDIR /app
RUN pip  --no-cache-dir install -r requirements.txt    

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
