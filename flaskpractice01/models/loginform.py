import wtforms
from flask_wtf import FlaskForm
from wtforms import validators

class LoginForm(FlaskForm):
    """
    form字段的参数
    label=None, 表单的标签
    validators=None, 校验，传入校验的方法
    filters=tuple(), 过滤
    description='',  描述
    id=None, html id
    default=None, 默认值
    widget=None, HTML样式
    render_kw=None, HTML属性 参数
    """
    username = wtforms.StringField(
        label="用户名",
        validators=[validators.DataRequired("用户名不能为空")],
        render_kw={
            "class":"form-control",
            "placeholder":"用户名"
        }
    )
    password = wtforms.PasswordField(
        label="密码:",
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "密码"
        }
    )
    password2 = wtforms.PasswordField(
        label="确认密码:",
        validators=[validators.DataRequired(),validators.EqualTo('password','密码不一致!')],
        render_kw={
            "class": "form-control",
            "placeholder": "确认密码"
        }

    )
    submit = wtforms.SubmitField(
        label='提交',
        render_kw={
            "class":"btn btn-primary btn-block"
        }
    )