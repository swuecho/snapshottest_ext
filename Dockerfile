FROM python:3.7.7-buster
WORKDIR /app
RUN pip install --upgrade pip wheel
ADD ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./ /app/
ENV PYTHONPATH=/app
RUN ls -la
RUN pip install -e .
RUN pytest snapshottest_ext/test -vv --junitxml=junit/test_results.xml

