from flask import jsonify
from app import app
from app.models.About import About
from app.models.Employment import Employment
from app.models.Portfolio import Portfolio
from app.models.Skills import Skills
from app.models.Studies import Studies
from app.models.Pdf import Pdf

from config import Config

from flask import jsonify, request,  send_file, make_response

app.config.from_object(Config)

@app.route('/about', methods=['GET'])
def get_about():
    all_about = About.query.all()
    about_data = [about.to_dict() for about in all_about]
    response = jsonify(about_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/jobs', methods=['GET'])
def get_jobs():
    all_jobs = Employment.query.all()
    jobs_data = [job.to_dict() for job in all_jobs]
    response = jsonify(jobs_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/portfolio', methods=['GET'])   
def get_portfolio():
    all_portfolio = Portfolio.query.all()
    portfolio_data = [portfolio.to_dict() for portfolio in all_portfolio]
    response = jsonify(portfolio_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/skills', methods=['GET'])
def get_skills():
    all_skills = Skills.query.all()
    skills_data = [skill.to_dict() for skill in all_skills]
    response = jsonify(skills_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/studies', methods=['GET'])
def get_studies():
    all_studies = Studies.query.filter(Studies.important == 1).order_by(Studies.dateEntry.desc()).all()
    studies_data = [study.to_dict() for study in all_studies]
    response = jsonify(studies_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/getPDF", methods=["GET"])
def get_pdf():
    pdf = Pdf()
    if pdf.convertHTMLtoPDF():
        try:
            pdf = open("HV_Edilson_Laverde_Molina.pdf", 'rb')
            response = make_response(pdf.read())
            response.headers['Content-Type'] = 'application/pdf'
            response.headers["Content-Disposition"] = "attachment; filename=HV_Edilson_Laverde_Molina.pdf"
            return response
        except Exception as e:
            return str(e)
    return False  