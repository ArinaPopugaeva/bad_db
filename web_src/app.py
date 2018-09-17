from bottle import Bottle, route, run

app = Bottle()

@app.route('/')
def index():
    return 'hello world'



app.run(host='localhost', port=8080, debug=True)