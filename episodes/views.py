from django.shortcuts import get_object_or_404, render

from .models import Episode

# Create your views here.
def index(request):
	episodes = Episode.objects.all()
	current_episode = Episode.objects.first()
	return render(request, 'episodes/index.html', {'episodes': episodes, 'current_episode': current_episode})


def episode(request, pk):
	episodes = Episode.objects.all()
	current_episode = get_object_or_404(Episode, number=pk)
	return render(request, 'episodes/index.html', {'episodes': episodes, 'current_episode': current_episode})


# # pk = primary keys
# def course_detail(request, pk):
# 	course = get_object_or_404(Course, pk = pk)
# 	return render(request, 'courses/course_detail.html', { 'course': course })


# def step_detail(request, course_pk, step_pk):
# 	# course_id is the auto generated foriegn key assignment
# 	step = get_object_or_404(Step, course_id = course_pk, pk = step_pk)
# 	return render(request, 'courses/step_detail.html', { 'step': step })
