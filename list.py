import importlib.metadata

# Retrieve and print all installed package names and versions
for dist in importlib.metadata.distributions():
    print(f"{dist.metadata['Name']}=={dist.version}")