import json
import subprocess
import sys


cmd='find -P /usr/lib*/python*/site-packages/* -maxdepth 0 -type d'
out=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
data = {'python_dirs': {'list': [d for d in out.split('\n') if d]}}
sys.stdout.write(json.dumps(data) + '\n')
