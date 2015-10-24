from django.shortcuts import render


def main(request):
	template = "ciudades/main.html"

	context = {}

	return render(request, template, context)
