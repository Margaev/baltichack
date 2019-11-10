#-*- coding: utf-8 -*-
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Choice, Post, Poll, Votes, City
from django.contrib.auth import get_user_model

User = get_user_model()


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'posts': Post.objects.all(),
            'cities': City.objects.all(),
        })
        return context

    def get_queryset(self):
        return Post.objects.all().order_by('-create_date')


class FilterCity(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(FilterCity, self).get_context_data(**kwargs)
        context.update({
            'posts': Post.objects.filter(city=self.city).order_by('-create_date'),
            'cities': City.objects.all(),
        })
        return context

    def get_queryset(self):
        self.city = get_object_or_404(City, title=self.kwargs['city'])
        return Post.objects.filter(city=self.city).order_by('-create_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'results.html'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        user = request.user
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        votes = Votes.objects.filter(user=user)
        if votes:
            user_polls = []
            need_to_add = False
            for v in votes:
                user_polls.append(v.choice.poll)
            if p not in user_polls:
                need_to_add = True
            if need_to_add:
                new_vote = Votes.create(user, selected_choice)
                new_vote.save()
                selected_choice.votes_count = Votes.objects.filter(choice=selected_choice).count()
                selected_choice.save()
            return HttpResponseRedirect(reverse('citizenopinion:results', args=(p.id,)))
            # return render(request, 'detail.html', {
            #     'post': p.post,
            #     'error_message': "You cant vote anymore",
            # })
        else:
            new_vote = Votes.create(user, selected_choice)
            new_vote.save()
            selected_choice.votes_count = Votes.objects.filter(choice=selected_choice).count()
            selected_choice.save()
        # selected_choice.votes += 1
        # selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('citizenopinion:results', args=(p.id,)))
