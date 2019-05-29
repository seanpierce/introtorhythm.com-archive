from django.shortcuts import get_object_or_404, render, redirect

from .models import Episode

# Create your views here.
def index(request):
	"""Serves the index page"""
	all_episodes = Episode.objects.all().filter(active=True)

	return render(request,
		'episodes/index.html',
		{
			'episodes': all_episodes,
			'recent_episodes': all_episodes[:10],
			'higest_episode_number': all_episodes.first().number,
			'current_episode': all_episodes.first()
		})


def episode(request, primary_key):
	"""Serves the specific episode page"""
	all_episodes = Episode.objects.all().filter(active=True)
	recent_10_episodes = all_episodes[:10]
	highest_episode = all_episodes[:1]
	highest_episode_number = highest_episode[0].number
	current_episode = get_object_or_404(Episode, number=primary_key)

	if (current_episode not in recent_10_episodes or current_episode == recent_10_episodes[9]):
		recent_10_episodes = [
			x for x in all_episodes
			if int(x.number) >= int(current_episode.number) - 1
			and int(x.number) <= int(current_episode.number) + 8
		]

	return render(request,
		'episodes/index.html',
		{
			'episodes': all_episodes,
			'recent_episodes': recent_10_episodes,
			'higest_episode_number': highest_episode_number,
			'current_episode': current_episode
		})

def live(request):
	return redirect('https://live.introtorhythm.com:8443/stream')


# # pk = primary keys
# def course_detail(request, pk):
# 	course = get_object_or_404(Course, pk = pk)
# 	return render(request, 'courses/course_detail.html', { 'course': course })


# def step_detail(request, course_pk, step_pk):
# 	# course_id is the auto generated foriegn key assignment
# 	step = get_object_or_404(Step, course_id = course_pk, pk = step_pk)
# 	return render(request, 'courses/step_detail.html', { 'step': step })
