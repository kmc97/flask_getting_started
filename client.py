import requests

def hello_name_requests():
    r = requests.get("http://vcm-3553.vm.duke.edu:5000/hello/name")
    hello_info = r.json()
    print(hello_info)

def name_request():
    r = requests.get("http://vcm-3553.vm.duke.edu:5000/name")
    name_info = r.json()
    print(name_info)

def distance_request():
    r = requests.post("http://vcm-3553.vm.duke.edu:5000/distance")
    distance_info = r.json()
    print(distance_info)


distance_request()
