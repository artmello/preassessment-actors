set -e

name="%{NAME}"
vendor="%{VENDOR}"
dsa_sig="%{DSAHEADER:pgpsig}"
rsa_sig="%{RSAHEADER:pgpsig}"
sig="%|DSAHEADER?{${dsa_sig}}:{%|RSAHEADER?{${rsa_sig}}:{(none)}|}|"

query_format="\{\"name\": \"${name}\", \"vendor\": \"${vendor}\", \"signature\": \"${sig}\"\}, "
rpm_list=$(rpm -qa --qf "${query_format}" | sed 's/, $//')

echo -e "{\"rpm_qa\": {\"entries\": [${rpm_list}]}}"
