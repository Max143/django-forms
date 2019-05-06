from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm


def contact(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():   # validating the form 

			# Cleaning data provided by user
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']

			print(name, email)  # used for printing the name in the terminal 

	form = ContactForm()
	context = {'form' : form}
	return render(request, 'forms/contact.html', context)
	


def snippet(request):
	if request.method == 'POST':
		form = SnippetForm(request.POST)
		if form.is_valid():
			form.save()
	form = SnippetForm()
	context = {'form':form}
	return render(request, 'forms/contact.html', context)