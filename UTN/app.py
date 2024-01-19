from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "This webpage has been viewed "+counter+" time(s)"

@app.route("/hello")
def hello_world_no_redis():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
