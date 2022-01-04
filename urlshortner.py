import bitly_api
from bitly_api import Connection
API_USER="username"
API_KEY="API_KEY"
bitly=bitly_api.Connection(API_USER,API_KEY)
result=bitly.shorten('https://copyassignment.com')
print(result)
