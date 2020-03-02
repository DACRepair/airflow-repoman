from setuptools import setup, find_packages

setup(
    name="airflow_repoman",
    version="0.0.1",

    author="Derek Vance",
    author_email="DACRepair@gmail.com",
    description="airflow-repoman is a DAG/Plugin repo manager for Airflow.",
    keywords="apache-airflow plugin airflow git repoman",
    url="https://github.com/DACRepair/airflow-repoman",

    packages=find_packages(),
    entry_points={
        'airflow.plugins': [
            'my_plugin = airflow_repoman.plugin:RepomanAirflowPlugin'
        ]
    }
)
