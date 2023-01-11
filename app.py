from flask import Flask, render_template
from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

app=Flask(__name__)

app.config['SECRET_KEY']=" hello columbia "

class NamerForm(FlaskForm):
    name=StringField("What's Your Name?", validators=[DataRequired()])
    submit=SubmitField("Submit") 
    

@app.route('/home')
def home():
    name_columbia="Columbia University Lamont-Doherty Earth Observatory"
    return render_template('home.html',name=name_columbia)

@app.route('/what', methods=['GET','POST'])
def what():
    name=None
    form=NamerForm()
    
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=' '
        
    
    return render_template("wtf.html",name = name,form = form)

@app.route('/about/<name>')
def about(name):
    return render_template('about.html',name=name)

@app.route('/contact')
def contact():
    return render_template('contact_us.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/giving')
def giving():
    return render_template('giving.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/people')
def people():
    return render_template('people.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/practice_navbar')
def practice_navbar():
    return render_template('practice_navbar.html')