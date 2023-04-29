import os
import requests
url = input("[+] Enter website URL: ")
response = requests.get(url)
filename = input("[+] Enter file name (without extension): ")
directory = input("[+] Enter directory to save file in (Required): ")
#save the shit -took me long enough to figure :cry:
if directory:
    filepath = os.path.join(directory, filename + ".html")
else:
    filepath = filename + ".html"

with open(filepath, "w") as f:
    f.write(response.text)
print(f"[-] HTML response saved to {filepath}")
