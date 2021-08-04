from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
from analysis import analysis_data
import pandas as pd


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
    df = pd.read_csv (r'./uploads/student_marks.csv')
    # columns
    colsName = df.columns.values.tolist()

    # Number of rows and columns
    colNumber = df.shape[1]
    rowNumber = df.shape[0]

    # mean 
    aveMark = df[colsName[-1]].mean()

    # median
    median = df[colsName[-1]].median()

    # lowest mark 
    minMark = df[colsName[-1]].min()

    # highest mark
    maxMark = df[colsName[-1]].max()

    df1 = df[(df.filter(like=colsName[-1]) >= 50).any(axis=1)]
    df2 = df[(df.filter(like=colsName[-1]) < 50).any(axis=1)]

    # "how many students got greater than 50"
    passedNumber = df1.shape[0]
    # "how many students got less than 50"
    failedNumber = df2.shape[0]

    basicStat = {
        "colsNames": colsName,
        "colNumber": colNumber,
        "rowNumber": rowNumber,
        "average": aveMark,
        "median": median,
        "minMark": minMark,
        "maxMark": maxMark,
        "passedNumber" : passedNumber,
        "failedNumber": failedNumber    
    }

    if request.method == 'POST':
        return 'redirected'
    else:
        return render_template('analysis.html', filename=file, basicStat=basicStat)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)