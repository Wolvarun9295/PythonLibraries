import os

print(f'Effective Group ID: {os.getegid()}')
print(f'Effective User ID {os.geteuid()}')
print(f'Real Group ID: {os.getgid()}')
print(f"List of Supplemental Group ID's {os.getgroups()}")
