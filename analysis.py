from flask import Blueprint

analysis_data = Blueprint('analysis', __name__)

@analysis_data.route("/analysis")
def dataAnalysis():
    return "list of accounts"