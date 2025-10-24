from flask import Flask, request, render_template
import client 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_msg():
    # get msg
    message = request.form['message']
    key = request.form['key']

    
    try:
        ack = client.send_single_message(message, key)  
    except Exception as e:
        return f"<h3>Error: {e}</h3>"

    return f"<h3>Message: {message} <br> Server acknowledgment: {ack}</h3>"

if __name__ == "__main__":
    app.run(debug=False)
