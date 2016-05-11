FROM jupyter/datascience-notebook

MAINTAINER Martin Ames Harrison <martinmartinharrisonharrison@gmail.com>

USER root
RUN apt-get upgrade && \
    apt-get update && \
    apt-get -y install \
    python-pip \
    libpq-dev \
    python-dev

#python development tools & other personal
RUN pip install pep8
RUN pip install pip-tools

#aws
RUN pip install boto3
RUN pip install s4cmd

#mysql connectors and high-level tools
RUN pip install db.py

# pandas + scikit-learn upgrade
RUN pip install pandas --upgrade
RUN pip install scikit-learn --upgrade

#pymc and its dependencies
RUN pip install --process-dependency-links git+https://github.com/pymc-devs/pymc3
RUN pip install patsy

#test libraries
RUN pip install pytest

# Jupyter Notebook Development Accompaniment
RUN pip install plotly
RUN apt-get install tree

USER jovyan