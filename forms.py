from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length


class TeamForm(FlaskForm):
    team_name = StringField("TEAM NAME", validators=[DataRequired(), Length(min=4, max=225)])
    submit = SubmitField("SUBMIT")


class ProjectForm(FlaskForm):
    project_name = StringField("PROJECT NAME", validators=[DataRequired(), Length(min=4, max=225)])
    description = TextAreaField("DESCRIPTION")
    completed = BooleanField("COMPLETED?")
    team_selection = SelectField("TEAM")
    submit = SubmitField("SUBMIT")
    
    def update_teams(self, teams):
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ]