import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', 
    errors='backslashreplace').split('\n')

print("Data retrieved: ")
print("data")
"""
@var profiles:
1. iterate over every element in returned <data> from command
2. if 'All User Profile' string is present in the element, then
3. extract the name of the connection
"""
profiles = [i.split(':')[1][1:-1] for i in data if 'All User Profile' in i]


for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8',
        errors='backslashreplace').split('\n')
        results = [b.split(':')[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30} | {:<}".format(i, results[0]))
        except:
            print("{:<30} | {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print("{<:30} | {:<}".format(i, "ENCODING ERROR"))

input("")
