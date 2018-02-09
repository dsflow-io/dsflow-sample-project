from IPython.display import display
from IPython.display import HTML, Markdown
import os
from pprint import *
import pandas as pd
import yaml
from jinja2 import Template
from textwrap import dedent
import subprocess
import sys
import glob

from .utils import get_datastore_path, get_flows_path


def show_tables():
    possible_tables = os.listdir(get_datastore_path() + '/tables')

    for p in sorted(possible_tables):
        print(p)


def load_table(type, table_name):
    if type == "parquet":
        return pd.read_parquet("/data/tables/%s" % table_name)

    elif type == "json":
        all_files = glob.glob(os.path.join("/data/raw/%s" % table_name, "*/*.json"))
        df_from_each_file = (pd.read_json(f, lines=True) for f in all_files)

        return pd.concat(df_from_each_file, ignore_index=True)

    elif type == "csv":
        all_files = glob.glob(os.path.join("/data/raw/%s" % table_name, "*/*.csv"))
        df_from_each_file = (pd.read_csv(f) for f in all_files)

        return pd.concat(df_from_each_file, ignore_index=True)
