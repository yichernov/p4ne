import requests, json, pprint
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify = False)

    print('ticket: ', response.json()['response']['serviceTicket'])
    return response.json()['response']['serviceTicket']

def get_devices(ticket):
    url = 'https://' + controller + '/api/v1/network-devices'
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json()

def get_topo(ticket):
    url = 'https://' + controller + '/api/v1/topology/physical-topology'
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json()

def get_hosts(ticket):
    url = 'https://' + controller + '/api/v1/hosts'
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = requests.get(url, headers=header, verify=False)
    return response.json()

@app.route('/')
def index():
    return render_template("topology.html")

@app.route('/api/topology')
def topology():
    return jsonify(get_topo(ticket)['response'])

if __name__ == '__main__':

    ticket = new_ticket()
    controller = 'devnetapi.cisco.com/sandbox/apic_em'
    url = 'https://' + controller + '/api/v1/host?limit=1&offset=1'
    header = {"content-type": "application/json", "X-Auth-Token": ticket}

    response = requests.get(url, headers = header, verify = False)

    print("Hosts = ")
    pprint.pprint(json.dumps(response.json()))

    app.run(debug = True)