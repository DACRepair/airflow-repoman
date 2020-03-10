# Airflow DAG Repo Manager
A plugin for [Apache Airflow](https://airflow.apache.org/).

##Setup:
At the moment, I have not set up binary builds, so adding it with pip will require a "git+< url >" entry.
###Prerequisites:
```
apache-airflow
click
cryptography
gitpython

# pip install apache-airflow click cryptography gitpython
```
>NOTE: Airflow must be installed and configured prior to plugin install.

###Installation:
>NOTE: This will install needed prerequisites
```bash
pip install git+https://github.com/DACRepair/airflow-repoman.git
```
Once this has been completed, you will need to verify your `dag_folder` is set to where you want it.
Open up a command line and run `airflow-repoman init`. If this does not work, verify that there is a binary in your bin folder.

## Usage:
###Airflow Webserver
To access the DAG Repos, simply navigate to Admin -> DAG Repos
![alt text] (https://github.com/DACRepair/airflow-repoman/blob/master/docs/img/adminmenu.png "Menu Location")