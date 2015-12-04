FROM jupyter/datascience-notebook

MAINTAINER Martin Ames Harrison <martinmartinharrisonharrison@gmail.com>

RUN apt-get -y install python-pip libpq-dev python-dev

RUN apt-get -y install openconnect

RUN ["/bin/bash", "-c", "source activate python2 && \
pip install sqlalchemy && \
source deactivate"]

RUN ["/bin/bash", "-c", "source activate python2 && \
pip install psycopg2 && \
source deactivate"]

RUN ["/bin/bash", "-c", "source activate python2 && \
pip install tabulate && \
source deactivate"]

RUN ["/bin/bash", "-c", "source activate python2 && \
pip install format-sql && \
source deactivate"]

RUN ["/bin/bash", "-c", "source activate python2 && \
pip install db.py && \
source deactivate"]

# Tensorflow
RUN ["/bin/bash", "-c", "source activate python2 && \
pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.5.0-cp27-none-linux_x86_64.whl && \
source deactivate"]

# Hive Querying
RUN apt-get -y install libsasl2-dev
RUN ["/bin/bash", "-c", "source activate python2 && \
pip install pyhs2 && \
source deactivate"]

# Redis
RUN ["/bin/bash", "-c", "source activate python2 && \
pip install redis && \
source deactivate"]

# MYSQL connector
RUN ["/bin/bash", "-c", "source activate python2 && \
pip install -Iv http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-1.2.3.zip#md5=6d42998cfec6e85b902d4ffa5a35ce86 && \
source deactivate"]

# PYMC3
RUN ["/bin/bash", "-c", "source activate python2 && \
pip install git+https://github.com/njsmith/scikits-sparse.git && \
source deactivate"]

ENV PYTHONPATH /home/jovyan/work/packages/boost_ds
