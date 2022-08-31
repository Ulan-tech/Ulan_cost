from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class CostForm(FlaskForm):
    customer = StringField('Customer', validators=[DataRequired(), Length(min=2, max=20)])

    layer_thickness = IntegerField('Layer thickness (mm)', validators=[DataRequired(), Length(min=2, max=20)])

    part_volume = IntegerField('Part volume (mm3)', validators=[DataRequired(), Length(min=2, max=20)])

    support_volume = IntegerField('Support volume (mm3)', validators=[DataRequired(), Length(min=2, max=20)])

    part_surface_area = IntegerField('Area of part surface(mm2)', validators=[DataRequired(), Length(min=2, max=20)])

    number_parts = IntegerField('Number of parts', validators=[DataRequired(), Length(min=2, max=20)])

    material = StringField('Material', validators=[DataRequired(), Length(min=2, max=20)])

    final_cost = SubmitField('Calculate the cost')



