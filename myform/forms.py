from django import forms
from .models import Snippet
# FROM CRISPY_FORMS
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core.validators import RegexValidator


'''
MultivalueFields 

It means One field that may have two or more sub-fields

'''


class NameWidget(forms.MultiWidget):

	def __init__(self, attrs=None):
		super().__init__([
			forms.TextInput	(),
			forms.TextInput()
			
		], attrs)

	def decompress(self, value):
		if value:
			return value.split(' ')
		return ['', '']
			# ['FirstValue', 'SecondValue']



class NameField(forms.MultiValueField):

	widget = NameWidget

	def __init__(self, *args, **kwargs):

		fields = (
			forms.CharField(validators=[RegexValidator(r'[a-zA-Z]+', 'Enter a valid first name (Only)')]),
			forms.CharField(validators=[RegexValidator(r'[a-zA-Z]+', 'Enter a valid first name (Only)')])
		)

		super().__init__(fields, *args, **kwargs)

	def compress(self, data_list):
		# data_list = ['FirstValue', 'SecondValue']
		return f'{data_list[0]} {data_list[1]}'
		# First value SecondValue


class ContactForm(forms.Form):
	name = NameField()  # MultiValued Feilds
	email = forms.EmailField(label='Email')
	category = forms.ChoiceField(choices = [('Question', 'Question'), ('Other', 'Other')])
	subject  = forms.CharField(required=False)
	body = forms.CharField(widget=forms.Textarea)

	'''
	Crispy form provide form helper which we use to specify the variety of attributes 
	inside of a form. 

	And we provide then can be used python to generate the html markup for us and 
	that will save us from doing lot of work. 

	'''

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper
		self.helper.form_method = 'POST'

		self.helper.layout = Layout(
			'name',
			'email',
			'category',
			'subject',
			'body',
			Submit('submit', 'Submit', css_class='btn btn-success')
		)




class SnippetForm(forms.ModelForm):

	class Meta:
		model = Snippet
		fields = ('name', 'body')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper
		self.helper.form_method = 'POST'

		self.helper.layout = Layout(
			'name',
			'body',
			Submit('submit', 'Submit', css_class='btn btn-success')
		)