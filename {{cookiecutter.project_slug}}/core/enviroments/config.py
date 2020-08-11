"""Create configuration enviroment.

What do you do need to config?
"""
import sys

config_file = 'core/enviroments/settings/' + sys.argv[1] + '.py'

# Read app.yaml template for GCP
with open(config_file) as file_name:
    data = file_name.read()

# Write file enviroment
with open(r'core/settings/settings.py', 'w') as file_name:
    file_name.write(data)
