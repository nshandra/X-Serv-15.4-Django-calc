from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import calculadora


def not_found(request):
    return HttpResponseNotFound("<html><body><h1>X-Serv-15.4-Django-calc</h1>"
                                "Usage: hostname:port/[operand1][+, -, *, /]"
                                "[operand2]</body></html>")


def calc_app(request, operand1, function, operand2):
    usage = "Usage: hostname:port/[operand1][+, -, *, /][operand2]"
    print(request)
    try:
        output = calculadora.calculator(function, operand1, operand2)
    except IndexError:
        output = usage
    print(output)

    return HttpResponse("<html><head><meta charset='utf-8'>"
                        "<h1>X-Serv-15.4-Django-calc</h1></head>"
                        "<body><p>" + str(output) + "</p></body></html>")
