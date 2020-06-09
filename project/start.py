from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user
from collections import namedtuple
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, datetime
from wtforms import SelectField

app = Flask(__name__)
app.secret_key = 'i love bmstu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

Message = namedtuple('Message', 'text tag')
messages = []
SignUp = namedtuple('SignUp', 'login password')
log_and_pass = []

username = '0'


class Doctors(db.Model):
    __tablename__ = 'doctors'
    id_doc = db.Column(db.Integer, primary_key = True)
    doc_name = db.Column(db.String(100), nullable = True)
    doc_spec = db.Column(db.String(100), nullable=True)
    doc_about = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Doctors %r>' % self.id_doc

class Schedule(db.Model):
    __tablename__ = 'schedule'
    id_sch = db.Column(db.Integer, primary_key = True)
    sch_name = db.Column(db.String(100), nullable = True)
    sch_spec = db.Column(db.String(100), nullable=True)
    sch_cab = db.Column(db.Integer, nullable=True)
    sch_floor = db.Column(db.Integer, nullable=True)
    sch_mon = db.Column(db.String(100), nullable=True)
    sch_tue = db.Column(db.String(100), nullable=True)
    sch_wed = db.Column(db.String(100), nullable=True)
    sch_thu = db.Column(db.String(100), nullable=True)
    sch_fri = db.Column(db.String(100), nullable=True)


    def __repr__(self):
        return '<Schedule %r>' % self.id_sch

class User(db.Model, UserMixin):
    __tablename__= 'sign_up'
    id_sign = db.Column(db.Integer, primary_key=True)
    sign_login = db.Column(db.String(100), nullable = True, unique = True)
    sign_password = db.Column(db.String(100), nullable=True)
    sign_role = db.Column(db.Integer, nullable=True)

    def get_id(self):
        return (self.id_sign)


class Record(db.Model):
    __tablename__ = 'record'
    id_rec = db.Column(db.Integer, primary_key = True)
    rec_login = db.Column(db.String(100), nullable = True)
    rec_date = db.Column(db.Date, default=datetime.utcnow)
    rec_diag = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return '<Record %r>' % self.id_rec

class News(db.Model):
    __tablename__ = 'news'
    id_news = db.Column(db.Integer, primary_key = True)
    news_date = db.Column(db.Date, default=datetime.utcnow)
    news_title = db.Column(db.String(300), nullable = True)
    news_text = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return '<News %r>' % self.id_news


class Doctor1(db.Model):
    __tablename__ = 'doc1'
    id_doc = db.Column(db.Integer, primary_key = True)
    doc_time = db.Column(db.String(50), nullable = True)
    doc_mon = db.Column(db.Integer, nullable = True)
    doc_tue = db.Column(db.Integer, nullable=True)
    doc_wed = db.Column(db.Integer, nullable=True)
    doc_thu = db.Column(db.Integer, nullable=True)
    doc_fri = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Doctor1 %r>' % self.id_doc

class Doctor2(db.Model):
    __tablename__ = 'doc2'
    id_doc = db.Column(db.Integer, primary_key = True)
    doc_time = db.Column(db.String(50), nullable = True)
    doc_mon = db.Column(db.Integer, nullable = True)
    doc_tue = db.Column(db.Integer, nullable=True)
    doc_wed = db.Column(db.Integer, nullable=True)
    doc_thu = db.Column(db.Integer, nullable=True)
    doc_fri = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Doctor2 %r>' % self.id_doc

class Doctor3(db.Model):
    __tablename__ = 'doc3'
    id_doc = db.Column(db.Integer, primary_key = True)
    doc_time = db.Column(db.String(50), nullable = True)
    doc_mon = db.Column(db.Integer, nullable = True)
    doc_tue = db.Column(db.Integer, nullable=True)
    doc_wed = db.Column(db.Integer, nullable=True)
    doc_thu = db.Column(db.Integer, nullable=True)
    doc_fri = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Doctor3 %r>' % self.id_doc

class Doctor4(db.Model):
    __tablename__ = 'doc4'
    id_doc = db.Column(db.Integer, primary_key = True)
    doc_time = db.Column(db.String(50), nullable = True)
    doc_mon = db.Column(db.Integer, nullable = True)
    doc_tue = db.Column(db.Integer, nullable=True)
    doc_wed = db.Column(db.Integer, nullable=True)
    doc_thu = db.Column(db.Integer, nullable=True)
    doc_fri = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Doctor4 %r>' % self.id_doc

class Notes(db.Model):
    __tablename__ = 'notes'
    id_notes = db.Column(db.Integer, primary_key = True)
    notes_day = db.Column(db.String(50), nullable = True)
    notes_time = db.Column(db.String(50), nullable=True)
    notes_user = db.Column(db.String(100), nullable=True)
    notes_doctor = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<Notes %r>' % self.id_notes

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/main', methods = ['GET'])
def main():
    return render_template('main.html', messages = messages)

@app.route('/doctors', methods = ['GET'])
def doctors():
    doc = Doctors.query.all()
    return render_template('doctors.html', doc = doc)

@app.route('/schedule', methods = ['GET'])
def schedule():
    sch = Schedule.query.all()
    return render_template('schedule.html', sch = sch)

@app.route('/contacts', methods = ['GET'])
def contacts():
    return render_template('contacts.html', messages = messages)

@app.route('/news', methods = ['GET'])
def news():
    news = News.query.all()
    return render_template('news.html', news = news)


@app.route('/user_space', methods = ['GET'])
def user_space():
    return render_template('user_space.html', messages = messages)

@app.route('/doctor_space', methods = ['GET'])
def doctor_space():
    return render_template('doctor_space.html', messages = messages)

@app.route('/admin_space', methods = ['GET'])
def admin_space():
    return render_template('admin_space.html', messages = messages)

@app.route('/add_new_diagnosis', methods = ['GET', 'POST'])
def add_new_diagnosis():
    if request.method == 'POST':
        login_patient = request.form['login_patient']
        diagnosis = request.form['diagnosis']

        new_diagnosis = Record(rec_login = login_patient, rec_diag = diagnosis)

        try:
            db.session.add(new_diagnosis)
            db.session.commit()
            return redirect(url_for('doctor_space'))
        except:
            return "Произошла ошибка!"

    else:
        return render_template('add_new_diagnosis.html', messages = messages)

@app.route('/add_news', methods = ['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        title = request.form['add_title']
        text = request.form['add_text']

        new_news = News(news_title = title, news_text = text)

        try:
            db.session.add(new_news)
            db.session.commit()
            return redirect(url_for('admin_space'))
        except:
            return "Произошла ошибка!"

    else:
        return render_template('add_news.html', messages = messages)

@app.route('/add_message', methods = ['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    messages.append(Message(text, tag))
    return redirect(url_for('main'))

@app.route('/patient_record', methods = ['GET'])
def patient_record():
    global username
    rec = Record.query.filter_by(rec_login=username).all()
    #rec = Record.query.all()
    return render_template('patient_record.html', rec=rec)

@app.route('/search_record', methods = ['GET', 'POST'])
def search_record():
    search_login = request.form.get('search_login')
    rec = Record.query.filter_by(rec_login=search_login).all()
    return render_template('search_record.html', rec=rec)

def add_records_to_schedule(doctor, day, time):
    global username
    doctor_name = ''
    if (doctor == 'doc1'):
        doctor_name = 'Мелконян Армен Георгиевич '
        if (day == 'monday'):
            rows = Doctor1.query.filter_by(doc_time=time).update({'doc_mon': 1})
        elif (day == 'tuesday'):
            rows = Doctor1.query.filter_by(doc_time=time).update({'doc_tue': 1})
        elif (day == 'wednesday'):
            rows = Doctor1.query.filter_by(doc_time=time).update({'doc_wed': 1})
        elif (day == 'thursday'):
            rows = Doctor1.query.filter_by(doc_time=time).update({'doc_thu': 1})
        elif (day == 'friday'):
            rows = Doctor1.query.filter_by(doc_time=time).update({'doc_fri': 1})
    if (doctor == 'doc2'):
        doctor_name = 'Алексеева Людмила Анатольевна'
        if (day == 'monday'):
            rows = Doctor2.query.filter_by(doc_time=time).update({'doc_mon': 1})
        elif (day == 'tuesday'):
            rows = Doctor2.query.filter_by(doc_time=time).update({'doc_tue': 1})
        elif (day == 'wednesday'):
            rows = Doctor2.query.filter_by(doc_time=time).update({'doc_wed': 1})
        elif (day == 'thursday'):
            rows = Doctor2.query.filter_by(doc_time=time).update({'doc_thu': 1})
        elif (day == 'friday'):
            rows = Doctor2.query.filter_by(doc_time=time).update({'doc_fri': 1})
    if (doctor == 'doc3'):
        doctor_name = 'Исаева Светлана Владимировна'
        if (day == 'monday'):
            rows = Doctor3.query.filter_by(doc_time=time).update({'doc_mon': 1})
        elif (day == 'tuesday'):
            rows = Doctor3.query.filter_by(doc_time=time).update({'doc_tue': 1})
        elif (day == 'wednesday'):
            rows = Doctor3.query.filter_by(doc_time=time).update({'doc_wed': 1})
        elif (day == 'thursday'):
            rows = Doctor3.query.filter_by(doc_time=time).update({'doc_thu': 1})
        elif (day == 'friday'):
            rows = Doctor3.query.filter_by(doc_time=time).update({'doc_fri': 1})
    if (doctor == 'doc4'):
        doctor_name = 'Новикова Яна Биктимировна'
        if (day == 'monday'):
            rows = Doctor4.query.filter_by(doc_time=time).update({'doc_mon': 1})
        elif (day == 'tuesday'):
            rows = Doctor4.query.filter_by(doc_time=time).update({'doc_tue': 1})
        elif (day == 'wednesday'):
            rows = Doctor4.query.filter_by(doc_time=time).update({'doc_wed': 1})
        elif (day == 'thursday'):
            rows = Doctor4.query.filter_by(doc_time=time).update({'doc_thu': 1})
        elif (day == 'friday'):
            rows = Doctor4.query.filter_by(doc_time=time).update({'doc_fri': 1})

    new_note = Notes(notes_day=day, notes_time=time, notes_user=username,
                     notes_doctor=doctor_name)
    db.session.add(new_note)
    db.session.commit()


@app.route('/go_to_doctor', methods = ['GET', 'POST'])
def go_to_doctor():
    form = Form()
    form.name.choices = [(doc.doc_name)for doc in Doctors.query.all()]
    name_of_doctor = ''
    # time = request.form.get('monday')

    if request.method == 'POST':
        name_of_doctor = form.name.data
        # time = request.form.get('monday')
        # print(time)
        if form.name.data == 'Мелконян Армен Георгиевич ':
            try:
                time = request.form['monday']
                add_records_to_schedule('doc1', 'monday', time)
            except:
                pass
            try:
                time = request.form['tuesday']
                add_records_to_schedule('doc1', 'tuesday', time)
            except:
                pass
            try:
                time = request.form['wednesday']
                add_records_to_schedule('doc1', 'wednesday', time)
            except:
                pass
            try:
                time = request.form['thursday']
                add_records_to_schedule('doc1', 'thursday', time)
            except:
                pass
            try:
                time = request.form['friday']
                add_records_to_schedule('doc1', 'friday', time)
            except:
                pass
            sch = Doctor1.query.all()
            return render_template('go_to_doctor.html', form=form, sch=sch)
        elif form.name.data == 'Алексеева Людмила Анатольевна':
            try:
                time = request.form['monday']
                add_records_to_schedule('doc2', 'monday', time)
            except:
                pass
            try:
                time = request.form['tuesday']
                add_records_to_schedule('doc2', 'tuesday', time)
            except:
                pass
            try:
                time = request.form['wednesday']
                add_records_to_schedule('doc2', 'wednesday', time)
            except:
                pass
            try:
                time = request.form['thursday']
                add_records_to_schedule('doc2', 'thursday', time)
            except:
                pass
            try:
                time = request.form['friday']
                add_records_to_schedule('doc2', 'friday', time)
            except:
                pass
            sch = Doctor2.query.all()
            return render_template('go_to_doctor.html', form=form, sch=sch)
        elif form.name.data == 'Исаева Светлана Владимировна':
            try:
                time = request.form['monday']
                add_records_to_schedule('doc3', 'monday', time)
            except:
                pass
            try:
                time = request.form['tuesday']
                add_records_to_schedule('doc3', 'tuesday', time)
            except:
                pass
            try:
                time = request.form['wednesday']
                add_records_to_schedule('doc3', 'wednesday', time)
            except:
                pass
            try:
                time = request.form['thursday']
                add_records_to_schedule('doc3', 'thursday', time)
            except:
                pass
            try:
                time = request.form['friday']
                add_records_to_schedule('doc3', 'friday', time)
            except:
                pass
            sch = Doctor3.query.all()
            return render_template('go_to_doctor.html', form=form, sch=sch)
        elif form.name.data == 'Новикова Яна Биктимировна':
            try:
                time = request.form['monday']
                add_records_to_schedule('doc4', 'monday', time)
            except:
                pass
            try:
                time = request.form['tuesday']
                add_records_to_schedule('doc4', 'tuesday', time)
            except:
                pass
            try:
                time = request.form['wednesday']
                add_records_to_schedule('doc4', 'wednesday', time)
            except:
                pass
            try:
                time = request.form['thursday']
                add_records_to_schedule('doc4', 'thursday', time)
            except:
                pass
            try:
                time = request.form['friday']
                add_records_to_schedule('doc4', 'friday', time)
            except:
                pass
            sch = Doctor4.query.all()
            return render_template('go_to_doctor.html', form=form, sch=sch)

    return render_template('go_to_doctor.html', form = form)

class Form(FlaskForm):
    name = SelectField('name',choices = [])


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    login = request.form.get('login')
    password = request.form.get('password')

    if request.method == 'POST':
        if login and password:
            user = User.query.filter_by(sign_login = login).first()
            if user and check_password_hash(user.sign_password, password):
                login_user(user)
                if user.sign_role == 1:
                    global username
                    username = login
                    return redirect(url_for('user_space'))
                elif user.sign_role == 2:
                    return redirect(url_for('doctor_space'))
                elif user.sign_role == 3:
                    return redirect(url_for('admin_space'))
            else:
                flash('Неправильный логин или пароль!')
        else:
            flash('Нет логина или пароля!')
    return render_template('sign_up.html')


@app.route('/log_out', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    global username
    username = '0'
    return redirect(url_for('hello_world'))

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    login = request.form.get('reg_login')
    password1 = request.form.get('reg_password1')
    password2 = request.form.get('reg_password2')
    role = request.form.get('role')

    if request.method == 'POST':
        if not (login or password1 or password2):
            flash('Заполните все поля!')
        elif password1 != password2:
            flash('Пароли не совпадают')
        else:
            hash_password = generate_password_hash(password1)
            new_user = User(sign_login = login, sign_password = hash_password, sign_role = role)
            db.session.add(new_user)
            db.session.commit()

    return render_template('registration.html', messages = messages)


@app.route('/create_schedule', methods = ['GET', 'POST'])
def create_schedule():
    form = Form()
    form.name.choices = [(doc.doc_name) for doc in Doctors.query.all()]
    if request.method == 'POST':
        name_of_doctor = form.name.data
        sch = Notes.query.filter_by(notes_doctor = name_of_doctor).all()
        return render_template('create_schedule.html', form = form, sch = sch)
    return render_template('create_schedule.html', form = form)






