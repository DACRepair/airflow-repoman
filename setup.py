from setuptools import setup

setup(
    name="airflow_repoman",
    entry_points={
        'airflow.plugins': [
            'my_plugin = airflow_repoman.plugin:RepomanAirflowPlugin'
        ]
    }
)
