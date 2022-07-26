# Flask implementation

from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
import numpy as np
from hero_dict import *
from engine import Engine
import os

import json

from nnpredictor import NNPredictor

# Creating a dictionary for choices

app = Flask(__name__, template_folder='html_templates')

app.config['SECRET_KEY'] = 'mysecretkey'


def get_api_string(recommendations, prob):
    recommendations = map(str, recommendations)
    return json.dumps({'x': recommendations, 'prob_x': prob})


class HeroForm(FlaskForm):

    radiant_hero_1 = SelectField(
        u'Pick First Radiant Hero:', choices=choice(heroes_json))
    radiant_hero_2 = SelectField(
        u'Pick Second Radiant Hero:', choices=choice(heroes_json))
    radiant_hero_3 = SelectField(
        u'Pick Third Radiant Hero:', choices=choice(heroes_json))
    radiant_hero_4 = SelectField(
        u'Pick Fourth Radiant Hero:', choices=choice(heroes_json))
    radiant_hero_5 = SelectField(
        u'Pick Fifth Radiant Hero:', choices=choice(heroes_json))
    dire_hero_1 = SelectField(u'Pick First Dire Hero:',
                              choices=choice(heroes_json))
    dire_hero_2 = SelectField(
        u'Pick Second Dire Hero:', choices=choice(heroes_json))
    dire_hero_3 = SelectField(u'Pick Third Dire Hero:',
                              choices=choice(heroes_json))
    dire_hero_4 = SelectField(
        u'Pick Fourth Dire Hero:', choices=choice(heroes_json))
    dire_hero_5 = SelectField(u'Pick Fifth Dire Hero:',
                              choices=choice(heroes_json))
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = HeroForm()
    if form.validate_on_submit():
        session['radiant_hero_1'] = form.radiant_hero_1.data
        session['radiant_hero_2'] = form.radiant_hero_2.data
        session['radiant_hero_3'] = form.radiant_hero_3.data
        session['radiant_hero_4'] = form.radiant_hero_4.data
        session['radiant_hero_5'] = form.radiant_hero_5.data
        session['dire_hero_1'] = form.dire_hero_1.data
        session['dire_hero_2'] = form.dire_hero_2.data
        session['dire_hero_3'] = form.dire_hero_3.data
        session['dire_hero_4'] = form.dire_hero_4.data
        session['dire_hero_5'] = form.dire_hero_5.data

        return redirect(url_for("recommendation"))

    return render_template('home.html', form=form)


@app.route('/recommendation')
def recommendation():

    radiant_team = [session['radiant_hero_1'],
                    session['radiant_hero_2'],
                    session['radiant_hero_3'],
                    session['radiant_hero_4'],
                    session['radiant_hero_5']]
    dire_team = [session['dire_hero_1'],
                 session['dire_hero_2'],
                 session['dire_hero_3'],
                 session['dire_hero_4'],
                 session['dire_hero_5']]
    my_team = radiant_team
    their_team = dire_team
    if len(my_team) >= 5:
        return 'Your Team is Full! Please remove a hero from your team.'
    else:
        prob_recommendation_pairs = Engine.recommend(my_team, their_team)
        recommendations = [hero for prob,
                           hero in prob_recommendation_pairs]
        prob = Engine.predict(my_team, their_team)
        return render_template('recommendation.html', prediction_text='{}'.format(get_api_string))


if __name__ == "__main__":
    app.debug = True
    app.run()
