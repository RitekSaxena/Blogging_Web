from django.shortcuts import render
from . models import Post , Comments, votes
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    posts = reversed(Post.objects.all())
    return render(request, 'posts/home.html', {'posts':posts})
@login_required
def detail(request, pk):
    post = Post.objects.get(id = pk)
    comments = reversed(Comments.objects.filter(post_related = post ))
    

    
    if request.method == 'POST':
   
        comment = Comments()

                
        comment.body = request.POST['body']
        comment.user = request.user
        comment.post_related = post
        comment.upvotes = 1
        comment.save()
        context = {'post':post , 'comments':comments}
        return render(request, 'posts/detail.html', context)

    else:

        
        comments = reversed(Comments.objects.filter(post_related = post ).order_by('upvotes'))
        context = {'post':post , 'comments':comments}
        return render(request, 'posts/detail.html', context)
@login_required
def upvote(request, pk , comm_id):
    post = Post.objects.get(id=pk)
    comm = Comments.objects.filter(id = comm_id)
    get_vote = votes.objects.filter(who = request.user , related_comment = comm)

    if get_vote is None:


        vote = votes()

        vote.who =  request.user
        vote.related_comment = comm
        vote.save()
        comm.upvotes +=1
        comm.save()
        comments = reversed(Comments.objects.filter(post_related = post ).order_by('upvotes'))
        context = {'post':post , 'comments':comments}
        return render(request, 'posts/detail.html', context)
    else:
        comments = reversed(Comments.objects.filter(post_related = post ).order_by('upvotes'))
        context = {'post':post , 'comments':comments}
        return render(request, 'posts/detail.html', context)


    

        