from flask import Flask, request, jsonify, render_template

## instantiate flask app
app = Flask(__name__,
    static_folder='static',
    template_folder='templates'
    ) 

### top page ###
@app.route('/', methods=['GET', 'POST'])
def page_top():
    return render_template('toppage.html') # rendering "templates/toppage.html"

### second page ###
@app.route('/2', methods=['GET', 'POST'])
def page_second():
	if request.method == 'GET':
		return render_template('page2.html') # rendering "templates/page2.html"
	elif request.method == 'POST':
		text = request.form['input_text'].upper() # get text from form -> uppercase
		return render_template('page2.html', return_text=text) # re-rendering "page2.html" with variable "return_text"

### third page ###
@app.route('/3', methods=['GET', 'POST'])
def page_third():
    return render_template('page3.html') # rendering "templates/page3.html"

## word length page - return character length of the word as JSON
@app.route('/<word>', methods=['GET', 'POST'])
def page_length(word):
    return jsonify({'word': word, 'length': len(word)})

if __name__ == "__main__":
    # debug=True -> reload automatically when update app.py
    app.run(host="0.0.0.0", port=8000, debug=True)