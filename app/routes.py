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
    all_jobs = Employment.query.order_by(Employment.dateEntry.desc()).all()
    jobs_data = [job.to_dict() for job in all_jobs]
    response = jsonify(jobs_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/portfolio', methods=['GET'])   
def get_portfolio():
    all_portfolio = Portfolio.query.filter_by(destaque=1).all()
    portfolio_data = [portfolio.to_dict() for portfolio in all_portfolio]
    response = jsonify(portfolio_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/portfolio/search', methods=['GET'])
def search_portfolio():
    query = request.args.get('query', '')
    if query:
        results = Portfolio.query.filter(
            (Portfolio.title.ilike(f'%{query}%')) |
            (Portfolio.subtitle.ilike(f'%{query}%')) |
            (Portfolio.description.ilike(f'%{query}%'))
        ).all()
        portfolio_data = [portfolio.to_dict() for portfolio in results]
    else:
        portfolio_data = Portfolio.query.all()
        portfolio_data = [portfolio.to_dict() for portfolio in portfolio_data]
        
    response = jsonify(portfolio_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/studies', methods=['GET'])
def get_studies():
    all_studies = Studies.query.order_by(Studies.dateEntry.desc()).all()
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