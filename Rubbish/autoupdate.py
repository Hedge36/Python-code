import os

packages = ["numpy", "matplotlib", "pandas"]
for pack in packages:
    os.sys("pip install -U %s" % pack)
