# Create your views here.
from django.http import HttpResponse
from lxml import html
from urllib2 import urlopen
from django.utils import simplejson
from django.shortcuts import render_to_response


def home(request):
    return render_to_response("index.html")


def query(request, page_id):
    print "got here"
    try:
        url = urlopen("http://ucb-anoncon.livejournal.com/7788.html?page=" + str(page_id))
        dom_data = html.parse(url)
        json = simplejson.loads(dom_data.getroot().cssselect("script#comments_json")[0].text)
        output = [{"comment": o["article"], "link": o["actions"][1]["href"]} for o in json if "article" in o.keys()]
        return HttpResponse(simplejson.dumps(output), mimetype="application/javascript")
    except Exception:
        print "uh oh"
        return HttpResponse(simplejson.dumps({}), mimetype="application/javascript")
    # comments += [o["article"] for o in loads(html.parse(urllib2.urlopen("http://ucb-anoncon.livejournal.com/7788.html?page=" + str(i))).getroot().cssselect("script#comments_json")[0].text) if "article" in o.keys()]

def query2(request, page_id):
    print "query 2"
    try:
        url = urlopen("http://ucb-anoncon.livejournal.com/7969.html?page=" + str(page_id))
        dom_data = html.parse(url)
        json = simplejson.loads(dom_data.getroot().cssselect("script#comments_json")[0].text)
        output = [{"comment": o["article"], "link": o["actions"][1]["href"]} for o in json if "article" in o.keys()]
        return HttpResponse(simplejson.dumps(output), mimetype="application/javascript")
    except Exception:
        print "uh oh"
        return HttpResponse(simplejson.dumps({}), mimetype="application/javascript")