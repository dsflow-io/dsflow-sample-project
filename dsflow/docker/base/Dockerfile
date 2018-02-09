FROM jupyter/scipy-notebook

RUN pip install httpie

RUN pip install plotnine

RUN pip install pandasql

RUN pip install pyarrow

RUN rm -r work

CMD start.sh jupyter lab
