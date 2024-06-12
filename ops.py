import requests

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def ping(url):
    r = requests.get(url)
    print(r.status_code)


ping('https://www.bbc.com')
