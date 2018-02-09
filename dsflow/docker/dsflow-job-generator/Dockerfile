FROM python:3

RUN pip install configparser && \
    pip install Click==6.7 && \
    pip install nbformat==4.4 && \
    pip install pyyaml==3.12 && \
    pip install "Jinja2<2.9.0,>=2.7.3" && \
    pip install xlwt==1.3 && \
    pip install requests && \
    pip install IPython && \
    pip install click-spinner && \
    pip install envparse==0.2.0

WORKDIR /usr/src/app

CMD "python dsflow-generate-job.py"
