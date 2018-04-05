from django.shortcuts import render
from django.http import HttpResponse
import calculadora

# Create your views here.

def calc_app(request):
    usage = "Usage: hostname:port/operand1/function/operand2"
    print(request)
    parsedRequest = request.path.split('/')[1:]
    print(parsedRequest)

    if '' in parsedRequest:
        output = usage
    else:
        try:
            output = calculadora.calculator(parsedRequest[1],
                                            parsedRequest[0],
                                            parsedRequest[2])
        except IndexError:
            output = usage
    print(output)

    return HttpResponse ("<html><head><meta charset='utf-8'>"
                         "<h1>Calculadora webApp</h1></head>"
                         "<body><p>" + str(output) + "</p></body></html>")