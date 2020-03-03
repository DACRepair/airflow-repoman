from airflow import settings

for section in settings.conf.sections():
    if len(settings.conf.options(section)) > 0:
        print("--------------------------")
        print("Section: {}".format(section))
        print("--------------------------")
        for option in settings.conf.options(section):
            print("{} = {}".format(option, settings.conf.get(section, option)))
