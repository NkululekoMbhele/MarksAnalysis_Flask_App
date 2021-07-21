from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
from analysis import analysis_data

app = Flask(__name__)

app.register_blueprint(analysis_data, url_prefix='/data')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['csvFile']
        filename = secure_filename(f.filename)
        f.save(f"./uploads/{filename}")
        
        return redirect(url_for('.analysis_data', file = filename))


@app.route('/analysis')
def analysis_data():
    file = request.args['file']
    if request.method == 'POST':
        return 'redirected'
    else:
        return render_template('analysis.html', name=file)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)