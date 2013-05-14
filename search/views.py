# Create your views here.
from django.http import HttpResponse
from lxml import html
from urllib2 import urlopen
from django.utils import simplejson
from django.shortcuts import render_to_response
from cgi import escape


def home(request):
    return render_to_response("index.html")


def query(request, page_id):
    output = do_the_querying("http://ucb-anoncon.livejournal.com/7788.html?page=", page_id)
    return HttpResponse(simplejson.dumps(output), mimetype="application/javascript")


def query2(request, page_id):
    print "query 2"
    output = do_the_querying("http://ucb-anoncon.livejournal.com/7969.html?page=", page_id)
    return HttpResponse(simplejson.dumps(output), mimetype="application/javascript")


def do_the_querying(url, page_id):
    try:
        url = urlopen(url + str(page_id))
        dom_data = html.parse(url)
        json = simplejson.loads(dom_data.getroot().cssselect("script#comments_json")[0].text)
        output = [{"comment": escape(o["article"]).replace(escape("<br />"), "<br />"), "link": o["actions"][1]["href"]} for o in json if "article" in o.keys() and o["article"] is not None]
        return output
    except Exception as e:
        print "somethings fucked up mate"
        print e
        return {}
