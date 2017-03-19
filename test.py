from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    # Render template
    return render_template('test.html')

@app.route('/json')
def json():
    # Response json
    return jsonify(
        success = True,
        data = {
            'foo': 'bar',
            'baz': 'qux'
        }
    )

# Run
if __name__ == '__main__':
    app.run(debug=True)
