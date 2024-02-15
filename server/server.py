from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    
    print('There is something beeing sent fucking Frontend. JUST TAKE IT MAN!!!!')
    data = {
        'message': 'Hello, world!'
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)