from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserProfile,History,Request,Interact

def Home(request):
    return render(request,"profiles/home.html",context=locals())


def about(request):
    return render(request,"profiles/about.html",context=locals())

'''
@login_required
def userProfile(request):
    user=request.user
    context={
        "user":user
    }
    return render(request,"profiles/profile.html",context)
'''


@login_required(login_url='accounts/login')
def userProfile(request, slug):

    profile = get_object_or_404(UserProfile, slug=slug)
    history=History.objects.filter(user=request.user)[::-1]
    amounts=History.objects.filter(user=request.user)
    sum=0
    for amount in amounts:
        sum+=amount.amount
    total=sum
    context = {
        'profile': profile,
        "history":history,
        "total":total
    }
    return render(request, 'profiles/profile.html', context)



class ProfileCreateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'createprofile.html'
    fields = ["first", "last", "bio", "picture"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = UserProfile.objects.all()
        return context



class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    template_name = 'createrequest.html'
    fields = ["title", "content","img"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RequestCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Request.objects.all()
        return context

'''

def homerequest(request):
    requests=Request.objects.all()
    context={
        "requests":requests,
    }
    
    return render(request,"homerequest.html",context)

def detail(request,id):
    reques=get_object_or_404(Request,id=id)
    interacts=reques.interact_set.all()
    votes=reques.interact_set.filter(upvote=True)
    print(votes)
    total=len(votes)

    if request.method=="POST":
        comment = request.POST.get('comment','')
        vote = request.POST.get('vote',False)
        user = request.user
        interact=Interact(comment=comment,upvote=vote,user=user)

    context={
        "reques":reques,
        "interact":interacts,
        "total":total
    }
    return render(request,"detail.html",context)

@login_required
def upvote(request,id):
    if request.method == 'POST':
        request = get_object_or_404(Request, pk=product_id)
        product.total_vote+=1
        product.save()
        return redirect('/products/' + str(product.id))
'''
'''
from django.views.generic import RedirectView


class ProductVoteToggle(RedirectView):

    def get_redirect_url(self, *args ,**kwargs):

        obj = get_object_or_404(Request, pk=self.kwargs['pk'])
        url_ = obj.get_absolute_url() 
        user = self.request.user
        if user.is_authenticated():
            if user in obj.votes_total.all():
                # you could remove the user if double upvote or display a message or what ever you want here
                obj.votes_total.remove(user)
            else:
                obj.votes_total.add(user)

        return url_
'''


