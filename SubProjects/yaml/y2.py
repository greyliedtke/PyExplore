import yaml

# Read YAML from a file
with open('yaml/e2.yaml', 'r') as file:
    loaded_data = yaml.load(file, Loader=yaml.FullLoader)
    print("\nLoaded data from 'example.yaml':")
    print(loaded_data)
