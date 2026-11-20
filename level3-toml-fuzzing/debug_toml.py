
import toml
import tomllib

document = "A = [1,"

print("Input:", repr(document))

# Test toml 0.10.2
try:
    result1 = toml.loads(document)
    print("toml accepted:", result1)
except Exception as error:
    print("toml rejected:", type(error).__name__, error)

# Test Python tomllib
try:
    result2 = tomllib.loads(document)
    print("tomllib accepted:", result2)
except Exception as error:
    print("tomllib rejected:", type(error).__name__, error)
