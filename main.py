#functions called when something happened

from flask import Flask, request

app = Flask(__name__)

@app.route("/test" , methods=["POST"])

#@app.route("/dipak12338/google-map" , methods=["POST"])

# def hook():
#	print(request.data)
#	return "Hello Pinnacle"
#

def webhook():
		if request.method == 'POST':
			print(request.json)
			return 'Success' , 200
		else:
			return 'Failed', 400
			
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=6000)
	#app.run(debug=True)