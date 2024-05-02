import pdfkit
import jinja2
from app.models.About import About
from app.models.Studies import Studies
from app.models.Employment import Employment
from app.models.Skills import Skills
from app.models.Portfolio import Portfolio
from app.models.References import References

import calendar
from flask import jsonify, request
import os
import locale
import base64
import os
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
class Pdf:
    def __init__(self):
        self.context = ''
    def pagePresentation(self):
        #consultamos la bd traemos todo el about
        all_about = About.query.all()
        about_data = [about.to_dict() for about in all_about]
        result = about_data
        info = result[0]
        #ahora listamos los estudios por importancia el campo important debe ser igual 1 
        all_studies = Studies.query.all()
        studies_data = [study.to_dict() for study in all_studies]
        school = studies_data

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
            'school':school,
            'linkedin':info['linkedin'],
            'github':info['github'],
            'gitlab':info['gitlab']
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
        all_jobs = Employment.query.order_by(Employment.dateEntry.desc()).all()
        jobs_data = [job.to_dict() for job in all_jobs]
        employment = jobs_data
        #revisamos las fechas string y las dejamos solo mes año
        for i in range(len(employment)):
            employment[i]['dateEntry'] = self.format_date(employment[i]['dateEntry'])
            employment[i]['dateEnd'] =  self.format_date(employment[i]['dateEnd'])
        #creamos un array y en cada pocicion agregamos 9 registros de emplo
        employment = [employment[i:i + 10] for i in range(0, len(employment), 10)]   
        # le agregamos mas contenido al self.context
        self.context['employment'] = employment

        #consultamos la bd traemos todo el skills
        all_skills = Skills.query.all()
        skills_data = [skill.to_dict() for skill in all_skills]
    
        skills = skills_data
        #creamos un array y en cada pocicion agregamos 9 registros del skill
        skills = [skills[i:i + 9] for i in range(0, len(skills), 6)]
        #le agregamos mas contenido al self.context
        self.context['skills'] = skills

        return employment
    def pageStudies(self):
       
        #ahora listamos los estudios por importancia el campo important debe ser igual 0
        all_studies = Studies.query.order_by(Studies.dateEnd.desc()).filter_by(important=0).all()
        studies_data = [study.to_dict() for study in all_studies]
        school = studies_data
        #le agregamos mas contenido al self.context
        self.context['complementarys'] = school
        return school
    def pagePortfolio(self):
        #consultamos la bd traemos todo el portafolio
        all_studies = Studies.query.all()
        studies_data = [study.to_dict() for study in all_studies]
        portafolio = studies_data
        #le agregamos mas contenido al self.context
        self.context['portfolio'] = portafolio
        return portafolio
    def pageReferencias(self):
        #consultamos la bd traemos todo el portafolio
        references = References.query.filter_by(type=1).all()
        
        #le agregamos mas contenido al self.context
        self.context['references_personal'] = references
        
        references = References.query.filter_by(type=0).all()
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
            with open("./app/template/images/icon"+str(i)+".png", "rb") as image:
                img_data = image.read()
            self.context['icon'+str(i)] = base64.b64encode(img_data).decode()
        with open("./app/template/images/persona.jpg", "rb") as image:
            img_data = image.read()
            self.context['profile'] = base64.b64encode(img_data).decode() 

        template_loader = jinja2.FileSystemLoader('./app/template/')
        template_dir = template_loader.searchpath[0]
        # Crear el ambiente de plantillas
        template_env = jinja2.Environment(loader=template_loader)
        # Obtener la plantilla HTML
        html_template = 'main.html'
        template = template_env.get_template(html_template)
        # Renderizar la plantilla con el contexto
        ouputString = template.render(self.context)
        # Configurar pdfkit
        #config = pdfkit.configuration(wkhtmltopdf=os.environ.get("WKHTMLTOPPDF"))
        #agregamos las opciones del pdf
        options = {
            'page-size': 'A4',
            'margin-top': '0.0in',
            'margin-right': '0.0in',
            'margin-bottom': '0.0in',
            'margin-left': '0.0in',
            'orientation': 'Portrait'
        }
        # Create a configuration object with the specified path
        config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
        try:
            # Convert HTML to PDF using the specified configuration app\template\css\styles.css
            pdfkit.from_string(ouputString, 'HV_Edilson_Laverde_Molina.pdf', configuration=config, options=options , css='/app/app/template/css/styles.css') 
        except Exception as e:
            print(f"Error during conversion: {e}")

        return True
