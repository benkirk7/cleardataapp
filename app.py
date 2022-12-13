import string
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/pangram")

# If the set of all letters of the alphabet are at least (>=) in the set created
# by the input string 'inString', then it is a pangram (true), else false.
# NOTE: using >= as superset to account for other things in the string, such as
# numbers, special characters, etc.
def isPangram():
    inString = request.args.get('key')
    return jsonify({"isPangram": set(inString.lower()) >= set(string.ascii_lowercase)}), 200



# To deploy on AWS
# 1. Log into AWS console.
# 2. Select EC2 (Amazon Elastic Compute Cloud) for capacity in the cloud.
# 3. Create the E2C used to deploy the app to.
# 4. SSH into the E2C.
# 5. Clone Flask app inside E2C.
# 6. Run a production-ready WSGI server - Gunicorn.
# 7. Run Nginx Webserver to accept and route request to Gunicorn.
