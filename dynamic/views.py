from django.shortcuts import render
from .models import Topics
# Create your views here.
def index(request):

    # topic1 = Topics()
    # topic1.name = 'Full Stack'
    # topic1.desc = 'Full stack using python and django framework'
    

    # topic2 = Topics()
    # topic2.name = 'Web Development'
    # topic2.desc = 'Web designing and development using python django'
    # topic2.img = 'undraw_Podcast_audience_re_4i5q.png'

    # topic3 = Topics()
    # topic3.name = 'MySQL'
    # topic3.desc = 'MySQL Databases'
    # topic3.img = 'undraw_Remote_design_team_re_urdx.png'

    # topics = [topic1,topic2, topic3]
    # # return render(request,"index.html", {'topic1' : topic1 , 'topic2' : topic2, 'topic3' : topic3})

    topics = Topics.objects.all()
    return render(request, "index.html", {'topics' : topics})



