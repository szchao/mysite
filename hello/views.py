from django.http import HttpResponse

def myview(request):
    num_vists = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_vists
    if num_vists > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count=' + str(num_vists))
    resp.set_cookie('dj4e_cookie', '7314392b', max_age=1000)
    return resp