from flask import Flask, render_template, url_for
import requests


app = Flask(__name__)
v_url = "http://10.2.0.20"
username = "ph-poc"
password = "ph-poc"
sim_name = "BDL-topology-wm4Rnk"
v_api_port = ":19399"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/blank')
def blank():
    return render_template('scratch.html')

@app.route('/error')
def error():
    return  render_template('404.html')

@app.route('/test')
def serial_con():

    c_mode = "webpage"
    c_port = 0

    params = {"mode": c_mode,
             "port": c_port
             }

    con_serial_api = "/simengine/rest/serial_port/" + sim_name
    con_serial_url = v_url + v_api_port + con_serial_api
    r = requests.get(con_serial_url, auth=(username, password), params=params)
    return render_template('test.html', result=r.json())

@app.route('/exp')
def exp_xml():
    exp_xml_api = "/simengine/rest/export/" + sim_name
    exp_xml_url = v_url + v_api_port + exp_xml_api
    r = requests.get(exp_xml_url, auth=(username, password))
    return r.content

@app.route('/list')
def list_sim():
    list_sim_api = "/simengine/rest/list"
    list_sim_url = v_url + v_api_port + list_sim_api
    r = requests.get(list_sim_url, auth=(username, password))
    return r.content



if __name__ == '__main__':
    app.run(debug=True)
