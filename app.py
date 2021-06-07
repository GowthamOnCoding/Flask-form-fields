from flask import Flask,render_template,url_for,redirect,session
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,
                    RadioField,SelectField,TextField,TextAreaField,SubmitField)
from wtforms.validators import Email,DataRequired,Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?',validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered')
    mood = RadioField('Please choose your mood?', 
          choices=[('mood_1','Happy'),('mood_2','Excited'),('mood_3','Sad')])
    food_choice = SelectField('Select your food ', 
                  choices=[('chi','Chicken'),('fi','Fish'),('mut','Mutton')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template('index.html',form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)