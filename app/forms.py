from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    battery = StringField('Заряд аккумулятора')
    battery_usage = StringField('Расход аккумулятора на метр полета')
    camera_angle = StringField('Угол обзора камеры')

    drone_dot_lon = StringField('Координаты дрона (долгота)', validators=[DataRequired()], id="dronX")
    drone_dot_lat = StringField('Координаты дрона (широта)', validators=[DataRequired()], id="dronY")

    first_dot_lon = StringField('Координаты первого угла территории (долгота)', validators=[DataRequired()], id="upLeftCornerX")
    first_dot_lat = StringField('Координаты первого угла территории (широта)', validators=[DataRequired()], id="upLeftCornerY")
    
    second_dot_lon = StringField('Координаты противоположного угла (долгота)', validators=[DataRequired()], id="downRightCornerX")
    second_dot_lat = StringField('Координаты противоположного угла (широта)', validators=[DataRequired()], id="downRightCornerY")
    
    submit = SubmitField('Построить маршрут')
