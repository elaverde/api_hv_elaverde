# -*- coding: utf-8 -*-
from api.config import db, app
from api.models.Employment import Employment
from api.models.EmploymentSchema import EmploymentSchema
from api.models.Studies import Studies
from api.models.StudiesSchema import StudiesSchema
from api.models.Portfolio import Portfolio
from api.models.PortfolioSchema import PortfolioSchema
from api.models.Skills import Skills
from api.models.SkillsSchema import SkillsSchema
from api.models.About import About
from api.models.AboutSchema import AboutSchema
from api.models.Pdf import Pdf
from flask import jsonify, request,  send_file, make_response


employmentSchema = EmploymentSchema(many=True)
studiesSchema = StudiesSchema(many=True)
portfolioSchema = PortfolioSchema(many=True)
skillsSchema = SkillsSchema(many=True)
aboutSchema = AboutSchema(many=True)





@app.route("/jobs", methods=["GET"])
def get_jobs():
    all_employment = Employment.query.order_by(Employment.dateEntry.desc()).all()
    result = employmentSchema.dump(all_employment)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route("/studies", methods=["GET"])
def get_studies():
    all_studies = Studies.query.order_by(Studies.dateEnd.desc()).all()
    result = studiesSchema.dump(all_studies)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route("/portfolio", methods=["GET"])
def get_portfolio():
    all_portfolio = Portfolio.query.all()
    result = portfolioSchema.dump(all_portfolio)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route("/skills", methods=["GET"])
def get_skills():
    all_skills = Skills.query.all()
    result = skillsSchema.dump(all_skills)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route("/about", methods=["GET"])
def get_about():
    all_about = About.query.all()
    result = aboutSchema.dump(all_about)
    response = jsonify(result[0])
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