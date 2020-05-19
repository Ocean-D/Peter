from wtforms import  Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired,Regexp

class SearchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)


class DriftForm(Form):
    recipient_name = StringField('收件人姓名',validators=[
        DataRequired(),Length(2,10,message='收件人姓名长度必须在2到20个字符之间')])

    mobile = StringField('手机号',validators=[
        DataRequired(),Regexp('^1[0-9]{10}$',0,message='请输入正确的手机号')])

    message = StringField('留言')

    address = StringField('收件地址',validators=[
        DataRequired(),Length(10,70,message='地址还不到10个字符吗？尽量写详细点。')])



