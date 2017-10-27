import json
import subprocess
import sys

report = []

inputs = json.load(sys.stdin)
for d in inputs['python_pkgs']['list']:
    if 'is not owned by any package' in d['pkg']:
        report.append(d['dir'] + ' is not owned by an RPM package')
data = {'python_report': {'report': report}}
sys.stdout.write(json.dumps(data) + '\n')
