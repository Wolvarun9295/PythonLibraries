# Imported HTTPConnection from http.client.
from http.client import HTTPConnection

# Creating an object conn of HTTPConnection class.
conn = HTTPConnection("www.google.com")
# Calling the request method from conn.
conn.request("GET", "/")
# Storing the response in loadThis variable.
loadThis = conn.getresponse()
# Storing the content of response in display variable.
display = loadThis.read()
print(display)
