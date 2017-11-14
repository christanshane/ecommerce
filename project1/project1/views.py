from django.http import HttpResponse
import datetime
def current_date(request):
    now = datetime.date.today()
    someday = datetime.date(2017,1,1)
    diff = now - someday;
    html = "<html><body>It is now {}</body></html>".format(str(diff.days)+" days Since January 1, 2017")
    return HttpResponse(html)
