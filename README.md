# Sample dsflow project

v-0.3.2-sandbox-pandas

This is a fork of the dsflow sandbox, adapted for Python and Pandas.

![dsflow logo](docs/src/dsflow-logo.png?raw=true "dsflow")

_IMPORTANT: This framework is not meant to be deployed to production systems._


**Contents:**

<!-- TOC depthFrom:2 depthTo:2 withLinks:1 updateOnSave:1 orderedList:0 -->

- [What is dsflow sandbox?](#what-is-dsflow-sandbox)
- [TL;DR;](#tldr)
- [Tech stack 360](#tech-stack-360)
- [Core principles](#core-principles)
- [Documentation](#documentation)
- [Current limitations / hacks](#current-limitations-hacks)

<!-- /TOC -->


## What is dsflow's sandbox?

This project enables you to prototype pipelines for batch data analytics. It is designed to work on your local computer, using a **command line interface** (CLI).

This is a proof-of-concept product, build to illustrate the "ds philosophy"--a certain way of organizing data and transformations.


## TL;DR;

- `brew cask install docker`: install or update Docker 🐳
- `git clone -b dsflow-sandbox-pandas https://github.com/dsflow-io/dsflow-sample-project`
- `cd dsflow-sample-project`
- `git checkout -b my_branch_name`: create your own branch
- `source init.sh`: initialize the dsflow environment and build docker images (_it might take over 10 minutes to download all sources_ ☕️)
- `dsflow`: see the list of dsflow commands
- `dsflow generate-job`: display the list of job templates
- `dsflow generate-job TEMPLATE_NAME JOB_NAME`: generate a job based on a template
- `dsflow start-jupyter`: open the default IDE in your browser (Jupyter Lab with pyspark) at http://localhost:8888/ (default password = `green3`)
- `dsflow run JOB_NAME [JOB_PARAMETERS]`: runs the job in its associated container
- `dsflow stop-all`: terminate all dsflow Docker containers

See [Documentation](#documentation) below for detailed instructions.


## Contents of dsflow-sample-project

The repository contains the source code of the jobs:

```
jobs/
├── download-car_speed_limits
├── sql-car_speed_limits_agg
├── table-camera_agg
├── table-car_speed_limits
└── table-meteo_agg
```

Run the jobs in order:

```
dsflow run download-car_speed_limits 2018-02-09
dsflow run table-car_speed_limits 2018-02-09
dsflow run sql-car_speed_limits_agg 2018-02-09

```

- The first job will download data and add it to `datastore/raw/`.
- The second and third jobs will create tables and add them to `datastore/tables/`.

After you run the first 3 jobs, you should have all resources in the `datastore/` directory. For instance:

```

datastore
├── managed-tables
├── raw
│   └── car_speed_limits
│       └── ds=2018-02-09
└── tables
    ├── car_speed_limits
    │   └── ds=2018-02-09
    └── car_speed_limits
        └── ds=2018-02-09
```


`table-camera_agg` and `table-meteo_agg` are two additional examples.


## Tech stack 360

Those are the defaults when adopting dsflow sandbox/Pandas:

- Run everything within containers  (using [Docker](https://www.docker.com/what-docker)).
- Query and transform data with Python Pandas.
- Store data as [Parquet files](https://parquet.apache.org/).
- Write code and iterate on your scripts using [Jupyter](http://jupyter.org/).
- Collaborate with your team using Github (or any [version control systems](https://en.wikipedia.org/wiki/Version_control)).


## Core principles

See https://github.com/dsflow-io/dsflow#core-principles


## Documentation

### Requirements on Mac

Brew and Python need to be installed on your system.
If not, execute in your terminal:

```
xcode-select --install
```

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```
brew install python
```

A recent version of Docker is needed:

```
brew cask install docker
```

Installation on Ubuntu: https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/


**Frequent issues when installing dsflow on macOS**

- xcode: If xcode is outdated, update it with the app store, or just move it to Trash.
- Python: dsflow CLI works with Python 2.7 and 3.3+ and only requires the `pyyaml` module in addition to core modules. Scripts with additional requirements will run in containers.
- Docker: make sure it's running before launching dsflow.
- Docker-compose: make sure it's up-to-date (dsflow requires support for version '3.3')


### Requirements on Windows

Use Windows 10 with Ubuntu subsystem:

https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4

(untested)


### Initialize dsflow

Inside the dsflow project directory:

```
source init.sh
```

**In depth:**

This will set up environment variables and provide a shortcut to dsflow commands.  
For instance, `dsflow tree` will execute `python dsflow/dsflow-tree.py`


### Show list of available commands

```
dsflow
```


### Show list of job templates

```
dsflow generate-job
```

Without argument, this command will show the list of job templates.


### Generate a job from a template

```
dsflow generate-job TEMPLATE_NAME JOB_NAME
```

In order to build a typical end-to-end data pipeline, you may use the following commands:

```
dsflow generate-job download_file datasetname           --> 1st job will download data
dsflow generate-job pandas_sql datasetname              --> 2nd job will help transform data into a parquet file ("table")
```

The jobs won't run automatically when calling `dsflow generate-job ...`

**Hint**: Discover open data source on https://data.opendatasoft.com/explore/?q=meteo


### Run a notebook programmatically (experimental):

```
dsflow run JOB_NAME [PARAMETERS]
```

For instance:

```
dsflow run create-table-meteoparis 2017-11-09
```

With `dsflow run`, each job will run in its own container.  
By default, job outputs are saved to `datastore/`.


**What happens when a notebook-based job is run by dsflow?**

1. render job specifications as defined in job_specs.yaml,
   and pass it as an environment variable.
2. launch proper container
3. execute nb-convert utility within the container
4. notebook reads job specifications from environment variable
5. notebook is rendered as html and saved to datastore
   (goal: provide easy debugging in case something goes wrong)



### Launch notebook environment to edit your notebooks

```
dsflow start-notebook
```

Default password is `green3`.

This command launches Jupyter Lab in a container: it's a full IDE, featuring notebooks and advanced code edition capabilities.

**In depth**

The main directories are mounted on this container: `jobs/`, `adhoc/`, `datastore/`.

`datastore/` is also mounted as `/data/` on the container. All paths pointing to the datastore (source or sink) should refer to `/data/` to provide consistent paths across containers.

(modify the default password: property `c.NotebookApp.password`
  in `dsflow/config/jupyter-conf/jupyter_notebook_config.py`)




### Pipeline creation and scheduling with Bash scripts

DAGs of jobs can be easily setup using Makefiles or Bash scripts:


```
dsflow run create-table-meteoparis 2017-11-09
```


## Anatomy of a dsflow project (for data scientists)

This is a description of the dsflow-sample-project.

```

├── adhoc                               --> adhoc notebooks
│
├── datastore                           --> jobs outputs are stored in the datastore
│   ├── job_runs                        --> notebook runs are rendered as html
│   │   ├── table-meteo_agg
│   │   └── table-car_speed_limits
│   ├── raw                             --> json, csv, raw logs, etc.
│   │   └── car_speed_limits
│   │       ├── ds=2017-12-01
│   │       ├── ds=2017-12-02
│   │       └── ds=2017-12-03
│   └── tables                          --> Parquet files
│       ├── car_speed_limits                       (automatically discover tables
│       │   ├── ds=2017-12-01                based on the sub-directory names)
│       │   ├── ds=2017-12-02
│       │   └── ds=2017-12-03
│       └── car_speed_limits_agg
│           ├── ds=2017-12-01
│           ├── ds=2017-12-02
│           └── ds=2017-12-03
│
│
├── jobs                                --> job definitions and scripts
│   ├── create-table-meteo_agg
│   ├── create-table-meteoparis
│   ├── dashboard-previsions_pluie_paris
│   └── download-meteoparis
│
└── tmp                                 --> temporary data (managed by containers)
    ├── jupyter
    └── ...

```


## Anatomy of the dsflow framework (for data engineers)

The source code of dsflow (`$DSFLOW_ROOT`) is organized in a way that enables full customization: create new CLI commands, add more docker images, create additional job templates.

```
dsflow
├── dsflow-assistant.py                 # edit the CLI scripts, or create new commands
├── dsflow-build-images.py
├── dsflow-compose.py
├── ...
│
├── config                              --> config files for Jupyter
│   ├── ipython-conf
│   │   └── profile_default
│   │       └── startup
│   │           ├── README
│   │           └── startup.py          # customize notebook startup code
│   └── jupyter-conf
│       └── jupyter_notebook_config.py  # customize Jupyter
│
├── docker                              # edit or create new docker images
│   ├── adminer
│   │   └── docker-compose.yaml
│   ├── base
│   │   ├── Dockerfile
│   │   └── docker-compose.yaml
│   ├── db
│   │   ├── Dockerfile
│   │   └── docker-compose.yaml
│   └── ...
│
├── python_scripts                       # these scripts are meant to be used
│   ├── __init__.py                      # in the context of docker containers
│   ├── custom_libraries                 
│   │   ├── cli_utils.py                 # these scripts can be imported
│   │   ├── helpers.py                   # in jupyter notebooks
│   │   └── utils.py
│   ├── dsflow-generate-job.py
│   ├── infer_schema.py
│   └── transform-ipynb-to-py.py
│
└── templates                            # edit or add new jobs templates
    ├── README.md
    └── jobs
        ├── pandas_sql
        │   ├── README.md.j2
        │   ├── job_specs.yaml.j2
        │   ├── notebook.py.j2
        │   └── template_specs.yaml
        ├── download_file
        │   ├── README.md.j2
        │   ├── job_specs.yaml.j2
        │   ├── script.sh.j2
        │   └── template_specs.yaml
        └── ...

```


## Troubleshooting

If you face an error, take a screenshot / copy the logs and create an issue in Github (or mail it to pm@dsflow.io)

### Stop all containers and reset all

- run `dsflow stop-all`
- restart Docker (on Mac, in the Docker menu)




## Current limitations / hacks

- Dsflow CLI uses python scripts to execute `docker-compose`... that's definitely NOT a great design. In the future we'll either use 100% bash scripts or use docker Python libraries.
- Currently, the `ds` partition is compulsory. We're not making it easy to use hourly or weekly partitions of data.
- Fact tables vs. dimension tables: this is pure convention... dsflow doesn't yet help you deal specifically with one type or the other. It's an issue when running `dsflow.load_tables()`: we assume that all tables are fact tables, and all partitions are loaded. In Spark SQL, a `ds` column is automatically added: it allows you to select the data from the latest partition (using for instance `WHERE ds = '2017-12-05'`).
