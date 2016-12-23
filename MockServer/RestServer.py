
# main.py

from flask import Flask, url_for, Response
from flask_classy import FlaskView, route
import random

class RoboSubRestApiView(FlaskView):
	def __init__(self):
		self.runStarted = False
	#Obstacle Avoidance Appendix 4	
	@route("/obstacleAvoidance/<courseName>/<teamCode>",methods=['POST'])
	def obstacleAvoidance(self,courseName,teamCode):
		entranceOptions=["1","2","3"]
		exitOptions=["X","Y","Z"]
		js = "{\"gateCode\":\"("+random.choice(entranceOptions)+\
			","+random.choice(exitOptions)+")\"}"
		resp = Response(js, status=200, mimetype='application/json')
		return resp
	#Automated Docking Appendix 5	
	@route("/automatedDocking/<courseName>/<teamCode>",methods=['POST'])
	def automatedDocking(self,courseName,teamCode):
		symbolOptions=["cruciform","triangle","circle"]
		colorOptions=["black","red","green","blue"]
		option1="{\"symbol\":\""+random.choice(symbolOptions)+\
			"\",\"color\":\""+random.choice(colorOptions)+"\"}"
		option2="{\"symbol\":\""+random.choice(symbolOptions)+\
			"\",\"color\":\""+random.choice(colorOptions)+"\"}"
		js = "{\"dockingBaySequence\":["+option1+","+option2+"]}"
		resp = Response(js, status=200, mimetype='application/json')
		return resp
	#Interop Challenge Appendix 6
	#Pinger Location Appendix 8
		
	#Heartbeat Appendix 9
	@route("/heartbeat/<courseName>/<teamCode>",methods=['POST'])
	def heartbeat(self,courseName,teamCode):
		content = request.json
		challanges = ["gates","obstacles","docking","pinger","interop","return"]
		js = "{\"success\":\"true\"}"
		resp = Response(js, status=200, mimetype='application/json')
		if(content["challenge"] not in challanges):
			resp = Response(js, status=400, mimetype='application/json')
		return resp
	#Run Appendix 10
	@route("/run/start/<courseName>/<teamCode>",methods=['POST'])
	def runStart(self,courseName,teamCode):
		if(not self.runStarted):
			self.runStarted = True
		js = "{\"success\":\"true\"}"
		resp = Response(js, status=200, mimetype='application/json')
		return resp
	@route("/run/end/<courseName>/<teamCode>",methods=['POST'])
	def runEnd(self,courseName,teamCode):
		if(self.runStarted):
			self.runStarted = False
		js = "{\"success\":\"false\"}"
		resp = Response(js, status=200, mimetype='application/json')
		return resp
	#Other
	@route("",methods=['POST','GET'])
	def index(self):
		js = "[\"Welcome To Hawk Test Server.\"]"
		resp = Response(js, status=200, mimetype='application/json')
		return resp

app = Flask(__name__)

RoboSubRestApiView.register(app, route_base='/', subdomain='')

if __name__ == "__main__":
    app.run()

