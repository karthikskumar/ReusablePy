import pip
try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain

def intellimport(package):
    if hasattr(package, "__len__") and (not isinstance(package, str)):
        package = list(package)
        for each in package:
            try:
                __import__(each)
            except ImportError:
                pipmain(['install', each])
                __import__(each)
    else:
        try:
            __import__(package)
        except ImportError:
            pipmain(['install', package])
            __import__(package)