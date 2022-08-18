from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class CostForm(FlaskForm):
    customer = StringField('Customer',
                          validators=[DataRequired(), Length(min=2, max=20)])
    layer_thickness = IntegerField()
    part_volume =
    support_volume =
    part_surface_area =
    number_parts =
    material = StringField('Material',
                          validators=[DataRequired(), Length(min=2, max=20)])

    final_cost = SubmitField('USD')



