from json import loads
from flask import Flask, render_template, flash, request, redirect, url_for, send_file, Response, make_response
import os
from forms import *
from dune import *

app = Flask(__name__)	#initialising flask
app.config.from_object(__name__)	#configuring flask
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = QueryIdForm(request.form)
    
    if(request.method=="POST"):
        if(form.validate()):
            query_id = request.form['query_id']
            print(query_id, "HEREEEEE")
            data = produce_query_results(query_id)
            #data = data.to_html(header="true", table_id="table")
            resp = make_response(data.to_csv())
            resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
            resp.headers["Content-Type"] = "text/csv"
            return resp
            '''return render_template("index.html", form = form, column_names=data.columns.values, row_data=list(data.values.tolist()),
                           link_column="Patient ID", zip=zip)'''
            
            
    return render_template("index.html", form = form, data="NA")	#render_template basically renders the html code of page mentioned as arg when needed

@app.route("/uniswap-data", methods=['GET', 'POST'])
def uniswap_data():

    if(request.method=="POST"):
        print("HEREEE POSTTT")
        data = produce_query_results(query_id=1531431)
        resp = make_response(data.to_csv())
        resp.headers["Content-Disposition"] = "attachment; filename=uniswap_latest_100000.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp

    return render_template("uniswap.html")	#render_template basically renders the html code of page mentioned as arg when needed

if(__name__ == "__main__"):
	app.run(host="localhost", port=8000, debug=True)