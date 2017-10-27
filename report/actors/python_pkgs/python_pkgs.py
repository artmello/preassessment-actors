import json
import subprocess
import sys

cmd='rpm -qf'
inputs = json.load(sys.stdin)
data = {'python_pkgs' : {'list': []}}
for d in inputs['python_dirs']['list']:
    out=subprocess.Popen(cmd + ' ' + d, shell=True, stdout=subprocess.PIPE).stdout.read()
    data['python_pkgs']['list'].append({'dir': d, 'pkg': out.strip()})
sys.stdout.write(json.dumps(data) + '\n')
