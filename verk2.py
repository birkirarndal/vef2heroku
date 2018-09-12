from sys import argv

import bottle
from bottle import *


@route("/")
def index():
    return """
    <h1>Verkefni 2</h1>
    <a href="/a">Liður A</a> -
    <a href="/b">Liður B</a>
    """

@route("/a")
def a():
    return """
    <h2>Verkefni 2 - A</h2>
    <a href="/sida/1">Siða 1</a> -
    <a href="/sida/2">Siða 2</a> -
    <a href="/sida/3">Siða 3</a> -
    <a href="/">Forsíða</a>
    """

@route("/sida/<id>")
def page(id):
    if id == "1":
        return "Þetta er siða 1 <br><a href='/a'>Til baka</a>"
    elif id == "2":
        return "Þetta er siða 2 <br><a href='/a'>Til baka</a>"
    elif id == "3":
        return "Þetta er siða 3 <br><a href='/a'>Til baka</a>"
    else:
        return "<h2 style='color:red'>Þessi síða finnst ekki</h2>"

@route("/b")
def b():
    return """
    <h2>Verkefni 2 - B</h2>
    <h3>Veldu uppáhalds bókstafinn þinn</h3>
    <a href="/sida2?bokstafur=a"><img src="myndir/A.png"></a>
    <a href="/sida2?bokstafur=b"><img src="myndir/B.png"></a>
    <a href="/sida2?bokstafur=c"><img src="myndir/C.png"></a>
    <a href="/sida2?bokstafur=d"><img src="myndir/D.png"></a>
    """

@route("/sida2")
def page():
    l = request.query.bokstafur
    if l == 'a':
        return "<h3>Þetta er minn uppáhaldsstafur:</h3><img src='myndir/A.png'>"
    if l == 'b':
        return "<h3>Þetta er minn uppáhaldsstafur:</h3><img src='myndir/B.png'>"
    if l == 'c':
        return "<h3>Þetta er minn uppáhaldsstafur:</h3><img src='myndir/C.png'>"
    if l == 'd':
        return "<h3>Þetta er minn uppáhaldsstafur:</h3><img src='myndir/D.png'>"
    else:
        return "<h2 style='color:red'>Þessi síða finnst ekki</h2>"



@error(404)
def villa(error):
    return "<h2 style='color:red'>Þessi síða finnst ekki</h2>"

@route('/myndir/<skra>')
def static_skrar(skra):
    return static_file(skra, root='myndir')

run(host='localhost', port=8080, reloader=True, debug=True)