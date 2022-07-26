from flask_wtf import FlaskForm, csrf
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from wtforms.fields import StringField
from wtforms.widgets import TextArea

##WTForm
class CreatePostForm(FlaskForm):
    body = CKEditorField("Post", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CommentForm(FlaskForm):
    comment = StringField("Comment", widget=TextArea(), validators=[DataRequired()])
    post_id = HiddenField("post_id")
    submit = SubmitField("submit comment")

class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")