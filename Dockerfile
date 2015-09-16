FROM ubuntu:15.04

RUN apt-get update \
  && apt-get -y --force-yes install git python python-setuptools python-pip

ADD ./thredds_data_stream_housekeeping.py ./thredds_data_stream_housekeeping.py
ADD ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD python ./thredds_data_stream_housekeeping.py
