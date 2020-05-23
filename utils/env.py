from os import environ

def getEnv(key, defVal):
    if environ.get('Foo') is not None:
        return environ.get('Foo')
    else:
        return defVal