from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TeamForm(FlaskForm):
    team_name = StringField("team name", validators=[DataRequired(), Length(min=4, max=225)])
    submit = SubmitField("submit")
