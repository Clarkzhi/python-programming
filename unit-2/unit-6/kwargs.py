import requests
def msg(name, **kwarges):
    print(name)
    for k, v in kwargs.items():
        print(k, '=', v)

#msg('John')

#msg('jane', age=50, job='rtist', adress='toronto')

#default arguments

def my_func(name, age=25, url='http://localhost', active=False):
    print(name, age, url, active)

my_func('John')

def web_crawler(start="https://www.bbc.co.uk", follow_links=False):
    first = requests.get(start).text

    if follow_links:
        pass
        #find all links on page, add to a list
        #process list, starting with first link
web_crawler('http://www.sciam.com')

    