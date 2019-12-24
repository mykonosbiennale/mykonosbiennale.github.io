from invoke import task

@task

def runserver(c):
    c.run("PYTHONHTTPSVERIFY=0; ./manage.py runserver --settings=mykonosbiennale.offline_settings")

def export_artists(c):
    c.run("PYTHONHTTPSVERIFY=0; ./manage.py export_artists - -settings = mykonosbiennale.offline_settings")

def export_filmfestival(c):
    c.run("PYTHONHTTPSVERIFY=0; ./manage.py export_filmfestival - -settings = mykonosbiennale.offline_settings")

def staticsitegen(c):
    c.run("PYTHONHTTPSVERIFY=0; ./manage.py staticsitegen --settings=mykonosbiennale.offline_settings")

