from flask import jsonify, request, send_file, make_response, session, redirect, url_for, render_template
from app import app, db
from app.models.About import About
from app.models.Employment import Employment
from app.models.Portfolio import Portfolio
from app.models.Skills import Skills
from app.models.Studies import Studies
from app.models.References import References
from app.models.User import User
from app.models.Pdf import Pdf
from functools import wraps

from config import Config

app.config.from_object(Config)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.get_json(silent=True)
    if not data:
        # Fallback for form data (HTML forms)
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = data.get('username')
        password = data.get('password')


    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        session['username'] = user.username
        
        # If it was a form submission, redirect to dashboard
        if not data:
            return redirect(url_for('dashboard'))
            
        return jsonify({"message": "Login successful", "user": user.to_dict()})
    
    if not data:
        # For form submission, show error page or login again
        return render_template('login.html', error="Invalid credentials")
        
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/dashboard')
@login_required
def dashboard():
    about = About.query.first()
    jobs = Employment.query.order_by(Employment.dateEntry.desc()).all()
    portfolio = Portfolio.query.order_by(Portfolio.id.desc()).all()
    skills = Skills.query.order_by(Skills.percentage.desc()).all()
    studies = Studies.query.order_by(Studies.dateEntry.desc()).all()
    return render_template('dashboard.html', 
                           about=about, 
                           jobs=jobs, 
                           portfolio=portfolio, 
                           skills=skills, 
                           studies=studies)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/about', methods=['GET'])
def get_about():
    all_about = About.query.all()
    about_data = [about.to_dict() for about in all_about]
    response = jsonify(about_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/about', methods=['PUT'])
@login_required
def update_about():
    data = request.get_json()
    about_info = About.query.first()
    if not about_info:
        return jsonify({"error": "About information not found"}), 404
    
    for key, value in data.items():
        if hasattr(about_info, key):
            setattr(about_info, key, value)
    
    db.session.commit()
    return jsonify({"message": "About updated successfully", "data": about_info.to_dict()})

# Jobs CRUD
@app.route('/jobs', methods=['GET'])
def get_jobs():
    all_jobs = Employment.query.order_by(Employment.dateEntry.desc()).all()
    jobs_data = [job.to_dict() for job in all_jobs]
    response = jsonify(jobs_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/jobs', methods=['POST'])
@login_required
def create_job():
    data = request.get_json()
    new_job = Employment(**data)
    db.session.add(new_job)
    db.session.commit()
    return jsonify(new_job.to_dict()), 201

@app.route('/jobs/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def handle_job(id):
    job = Employment.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(job.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            if hasattr(job, key):
                setattr(job, key, value)
        db.session.commit()
        return jsonify(job.to_dict())
    else:
        db.session.delete(job)
        db.session.commit()
        return jsonify({"message": "Job deleted"})

# Portfolio CRUD
@app.route('/portfolio', methods=['GET'])   
def get_portfolio():
    all_portfolio = Portfolio.query.all()
    portfolio_data = [portfolio.to_dict() for portfolio in all_portfolio]
    response = jsonify(portfolio_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/portfolio', methods=['POST'])
@login_required
def create_portfolio():
    data = request.get_json()
    new_item = Portfolio(**data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@app.route('/portfolio/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def handle_portfolio(id):
    item = Portfolio.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(item.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        db.session.commit()
        return jsonify(item.to_dict())
    else:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Deleted"})

# Skills CRUD
@app.route('/skills', methods=['GET'])
def get_skills():
    all_skills = Skills.query.all()
    skills_data = [skill.to_dict() for skill in all_skills]
    response = jsonify(skills_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/skills', methods=['POST'])
@login_required
def create_skill():
    data = request.get_json()
    item = Skills(**data)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/skills/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def handle_skill(id):
    item = Skills.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(item.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        db.session.commit()
        return jsonify(item.to_dict())
    else:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Deleted"})

# Studies CRUD
@app.route('/studies', methods=['GET'])
def get_studies():
    all_studies = Studies.query.order_by(Studies.dateEntry.desc()).all()
    studies_data = [study.to_dict() for study in all_studies]
    response = jsonify(studies_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/studies', methods=['POST'])
@login_required
def create_study():
    data = request.get_json()
    item = Studies(**data)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/studies/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def handle_study(id):
    item = Studies.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(item.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        db.session.commit()
        return jsonify(item.to_dict())
    else:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Deleted"})


from sqlalchemy import text

@app.route('/db-init')
def db_init():
    try:
        db.create_all()
        # Fix column length by converting to TEXT
        db.session.execute(text('ALTER TABLE user MODIFY COLUMN password_hash TEXT'))
        db.session.commit()
        return jsonify({"message": "Database initialized and column converted to TEXT"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# Initial User Setup

@app.route('/init-user', methods=['POST'])
def init_user():
    if User.query.first():
        return jsonify({"error": "User already exists"}), 400
    data = request.get_json()
    user = User(username=data.get('username'), email=data.get('email'))
    user.set_password(data.get('password'))
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"})

# PDF Service
@app.route("/servicio", methods=["GET"])
def get_pdf():
    pdf = Pdf()
    if pdf.convertHTMLtoPDF():
        try:
            pdf_file = open("HV_Edilson_Laverde_Molina.pdf", 'rb')
            response = make_response(pdf_file.read())
            response.headers['Content-Type'] = 'application/pdf'
            response.headers["Content-Disposition"] = "attachment; filename=HV_Edilson_Laverde_Molina.pdf"
            pdf_file.close()
            return response
        except Exception as e:
            return str(e)
    return jsonify({"error": "Failed to generate PDF"}), 500

