from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField, SelectField
from wtforms.validators import DataRequired

class PlanVueloForm(FlaskForm):
    nombre = StringField('Nombre del vuelo', validators=[DataRequired()])
    fecha = DateField('Fecha de vuelo', format='%Y-%m-%d', validators=[DataRequired()])
    duracion = StringField('Duracion', validators=[DataRequired()])
    periocidad = SelectField('Seleccione', choices=[
    ('', 'Seleccione'),
    ('D1', 'Diario'),
    ('Q2', 'Quincenal'),
    ('M3', 'Mensual'),
    ('T4', 'Trimestral'),
    ('S5', 'Semestral')], validators=[DataRequired()])
    dat_bitacora = StringField('Bitácora', validators=[DataRequired()])
    id_cuaderno = HiddenField('Id cuaderno', validators=[DataRequired()])
    vuelos_estimados = HiddenField('Vuelos estimados', validators=[DataRequired()])
    submit = SubmitField('Guardar')
