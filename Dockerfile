FROM python:3.7.2
WORKDIR /app
RUN pip install --upgrade pip
ADD ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=snapshottest_ext
RUN ["python", "-m pytest", "tests", '-vv' "--junitxml=junit/test_results.xml"]

