from flask import Flask, render_template, request, jsonify

server = Flask(__name__)

@server.route("/")
def hello():
   return "Hello from NeqSim API!"

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=5000)