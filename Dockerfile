FROM python:3.7.2
WORKDIR /app
RUN pip install --upgrade pip
ADD ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./snapshottest_ext /app
ENV PYTHONPATH=/app
RUN ["python", "-m pytest", "tests", '-vv' "--junitxml=junit/test_results.xml"]

