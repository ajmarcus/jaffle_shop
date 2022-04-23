import os

for root, dirs, files in os.walk("/home/pyodide/"):
    for filename in files:
        print(f"{root}{filename}")

