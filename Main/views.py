from django.shortcuts import render

def HomePage(request):
    return render(request, 'HomePage.html', {})

def LabPage(request):
    return render(request, 'LabPage.html', {})

'''
#일정시간 마다 코드 실행하는 법
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print("Doing stuff...")
    # do your stuff
    s.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()
'''