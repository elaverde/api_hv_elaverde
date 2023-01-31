import pdfkit
import jinja2
from api.models.About import About
from api.models.AboutSchema import AboutSchema
from api.models.Studies import Studies
from api.models.StudiesSchema import StudiesSchema
from api.models.Employment import Employment
from api.models.EmploymentSchema import EmploymentSchema
from api.models.Skills import Skills
from api.models.SkillsSchema import SkillsSchema
from api.models.Portfolio import Portfolio
from api.models.PortfolioSchema import PortfolioSchema
from api.models.References import References
from api.models.ReferencesSchema import ReferencesSchema

import calendar
from flask import jsonify, request
import os
import locale
import base64
from dotenv import load_dotenv
import os
load_dotenv()
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
class Pdf:
    def __init__(self):
        self.context = ''
    def pagePresentation(self):
        #consultamos la bd traemos todo el about
        aboutSchema = AboutSchema(many=True)
        all_about = About.query.all()
        result = aboutSchema.dump(all_about)
        info = result[0]
        #ahora listamos los estudios por importancia el campo important debe ser igual 1 
        studiesSchema = StudiesSchema(many=True)
        all_studies = Studies.query.filter_by(important=1).all()
        result = studiesSchema.dump(all_studies)
        school = result

        # Crear el contexto para la plantilla
        self.context = {
            'name':info['name'],
            'lastname':info['lastname'],
            'email':info['email'],
            'site': info['site'],
            'address': info['address'],
            'phone': info['phone'],
            'degree':info['degree'],
            'dni': info['dni'],
            'civil_status': info['civil_status'],
            'city':info['city'],
            'birthdate':info['birthdate'],
            'about':info['about'],
            'school':school
        }
        return info 
    def format_date(self,date):
        if date == None:
            return None
        #convertimos la fecha a mes y año
        date = str(date)[:7]
        #convertimos el mes a letra
        date = date.split('-')
        #hacemos un try para posible errores fechas 
        try:
            month = calendar.month_name[int(date[1])]
            month = month.title()
            
        except:
            month = ''
        date = month + ' ' + date[0]
        return date  
    def pageJobsSkills(self):
        # Crear el contexto para la plantilla
        employmentSchema = EmploymentSchema(many=True)
        all_employment = Employment.query.order_by(Employment.dateEntry.desc()).all()
        result = employmentSchema.dump(all_employment)
        employment = result
        #revisamos las fechas string y las dejamos solo mes año
        for i in range(len(employment)):
            employment[i]['dateEntry'] = self.format_date(employment[i]['dateEntry'])
            employment[i]['dateEnd'] =  self.format_date(employment[i]['dateEnd'])
        #creamos un array y en cada pocicion agregamos 9 registros de emplo
        employment = [employment[i:i + 10] for i in range(0, len(employment), 10)]   
        # le agregamos mas contenido al self.context
        self.context['employment'] = employment

        #consultamos la bd traemos todo el skills
        skillsSchema = SkillsSchema(many=True)
        all_skills = Skills.query.all()
        result = skillsSchema.dump(all_skills)
        skills = result
        
        #creamos un array y en cada pocicion agregamos 9 registros del skill
        skills = [skills[i:i + 9] for i in range(0, len(skills), 6)]
        #le agregamos mas contenido al self.context
        self.context['skills'] = skills

        return employment
    def pageStudies(self):
       
        #ahora listamos los estudios por importancia el campo important debe ser igual 0
        studiesSchema = StudiesSchema(many=True)
        all_studies = Studies.query.order_by(Studies.dateEnd.desc()).filter_by(important=0).all()
        result = studiesSchema.dump(all_studies)
        school = result
        #le agregamos mas contenido al self.context
        self.context['complementarys'] = school
        return school
    def pagePortfolio(self):
        #consultamos la bd traemos todo el portafolio
        portafolioSchema = PortfolioSchema(many=True)
        all_portafolio = Portfolio.query.all()
        result = portafolioSchema.dump(all_portafolio)
        portafolio = result
        #le agregamos mas contenido al self.context
        self.context['portfolio'] = portafolio
        return portafolio
    def pageReferencias(self):
        #consultamos la bd traemos todo el portafolio
        referencesSchema = ReferencesSchema(many=True)
        all_references = References.query.filter_by(type=1).all()
        result = referencesSchema.dump(all_references)
        references = result
        #le agregamos mas contenido al self.context
        self.context['references_personal'] = references
        referencesSchema = ReferencesSchema(many=True)
        #consultamos la bd traemos todo el portafolio
        all_references = References.query.filter_by(type=0).all()
        result = referencesSchema.dump(all_references)
        references = result
        #le agregamos mas contenido al self.context
        self.context['references_familiar'] = references
        return references
    
    def convertHTMLtoPDF(self):
        info = self.pagePresentation()
        info = self.pageJobsSkills()
        info = self.pageStudies()
        info = self.pagePortfolio()
        info = self.pageReferencias()

        #leemos loo 10 icon con un for
        for i in range(1,11):
            with open("./api/template/images/icon"+str(i)+".png", "rb") as image:
                img_data = image.read()
            self.context['icon'+str(i)] = base64.b64encode(img_data).decode()
        with open("./api/template/images/persona.jpg", "rb") as image:
            img_data = image.read()
            self.context['profile'] = base64.b64encode(img_data).decode() 

        template_loader = jinja2.FileSystemLoader('./api/template/')
        template_dir = template_loader.searchpath[0]
        # Crear el ambiente de plantillas
        template_env = jinja2.Environment(loader=template_loader)
        # Obtener la plantilla HTML
        html_template = 'main.html'
        template = template_env.get_template(html_template)
        # Renderizar la plantilla con el contexto
        ouputString = template.render(self.context)
        # Configurar pdfkit
        config = pdfkit.configuration(wkhtmltopdf=os.environ.get("WKHTMLTOPPDF"))
        #agregamos las opciones del pdf
        options = {
            'page-size': 'A4',
            'margin-top': '0.0in',
            'margin-right': '0.0in',
            'margin-bottom': '0.0in',
            'margin-left': '0.0in',
            'orientation': 'Portrait'
        }
        # Generar el PDF con la hoja de estilos especificada
        pdfkit.from_string(ouputString, 'HV_Edilson_Laverde_Molina.pdf', configuration=config, options=options ,  css='./api/template/css/styles.css') 
        return True
