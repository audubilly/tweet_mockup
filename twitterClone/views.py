from django.shortcuts import render, redirect

from .forms import TweetForm
from .models import TweetModel


def post_tweet(request):
    all_tweets = TweetModel.objects.all()
    if request.method != 'POST':

        form = TweetForm()
        context = {
            'form': form,
            'all_tweets': all_tweets

        }
        return render(request, 'create_tweet.html', context)
    else:
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_tweet')



# Create your views here.
