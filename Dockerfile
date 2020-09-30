FROM python:3.7.7-buster
WORKDIR /app
RUN pip install --upgrade pip wheel
ADD ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./snapshottest_ext /app
ENV PYTHONPATH=/app
RUN pytest tests -vv --junitxml=junit/test_results.xml

