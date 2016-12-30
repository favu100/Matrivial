from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import numpy as np;
from sympy import *

def index(request):
    A = Matrix([[1,2],[3,4]])
    return HttpResponse(A @ A)


