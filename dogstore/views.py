from django.shortcuts import render

def handler404(request, exception):
    """ Error Handler for 404s - Page Not Found """
    return render(request, "errors/404.html", status=404)