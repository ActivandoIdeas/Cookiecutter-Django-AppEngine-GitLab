"""Create enviroment variables.

What do you do need to build?
"""
import datetime
import sys

import yaml

# Read app.yaml template for GCP
with open('core/enviroments/app.yaml') as file_name:
    data = yaml.safe_load(file_name)

# Set enviroment variables for deploy
data['env_variables']['host'] = sys.argv[1]
data['env_variables']['database'] = sys.argv[2]
data['env_variables']['user'] = sys.argv[3]
data['env_variables']['password'] = sys.argv[4]
data['env_variables']['domain'] = sys.argv[5]
data['env_variables']['key'] = sys.argv[6]
data['env_variables']['frontend'] = sys.argv[7]
data['env_variables']['production'] = sys.argv[8]
data['env_variables']['staging'] = sys.argv[9]
data['env_variables']['gcpbucked'] = sys.argv[10]
data['env_variables']['project'] = sys.argv[11]
data['env_variables']['credentials'] = sys.argv[12]
data['env_variables']['passwordtest'] = sys.argv[13]
data['env_variables']['date'] = datetime.datetime.now().strftime(
    '%d/%m/%Y %H:%M:%S'
)
dict_file = data

# Write file enviroment
with open(r'app.yaml', 'w') as file_name:
    data = yaml.dump(data, file_name, sort_keys=False)
