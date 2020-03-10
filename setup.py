from setuptools import setup, find_packages

setup(
    name="airflow_repoman",
    version="0.2.0",

    author="Derek Vance",
    author_email="DACRepair@gmail.com",
    description="airflow-repoman is a DAG/Plugin repo manager for Airflow.",
    keywords="apache-airflow plugin airflow git repoman",
    url="https://github.com/DACRepair/airflow-repoman",

    packages=find_packages(),
    include_package_data=True,
    install_requires=['apache-airflow',
                      'click',
                      'gitpython'],

    entry_points={'airflow.plugins': ['airflow_repoman = airflow_repoman.plugin:RepomanAirflowPlugin'],
                  'console_scripts': ['airflow-repoman = airflow_repoman.cli:main']}
)
