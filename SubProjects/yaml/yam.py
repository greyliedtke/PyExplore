import yaml

# Example data
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'skills': ['Python', 'JavaScript', 'Data Science']
}

# Convert Python data to YAML
yaml_data = yaml.dump(data, default_flow_style=False)
print("YAML representation:")
print(yaml_data)

# Write YAML to a file
with open('example.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
    print("YAML data written to 'example.yaml'")

# Read YAML from a file
with open('example.yaml', 'r') as file:
    loaded_data = yaml.load(file, Loader=yaml.FullLoader)
    print("\nLoaded data from 'example.yaml':")
    print(loaded_data)
