from django.shortcuts import render ,get_object_or_404,redirect
from .models import Post
from .forms import BlogPostForm  
from django.db.models import Q
# Create your views here. 

def posts_list(request):  
    posts=Post.objects.all()
    return render(request, "posts/posts_list.html" ,{'posts':posts})  
    
def post_detail(request, id):  
    post=get_object_or_404(Post, pk=id)
    return render(request, 'posts/post_detail.html',{'post':post})  
    
def post_add(request):   
    if request.method =='POST':   
        form=BlogPostForm(request.POST, request.FILES)    
        if form.is_valid(): 
            print("is valid")
            form.save()
            return redirect("posts_list") 
        else:
             return render(request, "posts/post_form.html",{"form": form})
    else:  
        form = BlogPostForm()
    return render(request, "posts/post_form.html",{"form": form})  
        
def edit_post(request, id):   
    post=get_object_or_404(Post, pk=id)
    if request.method=='POST':      
        form=BlogPostForm(request.POST, request.FILES, instance=post) 
        if form.is_valide(): 
            form.save() 
            return redirect("post_detail", id=id )  
         else:
             return render(request, "posts/post_form.html",{"form": form})   
            
    else: 
        post=get_object_or_404(Post, pk=id)
        form = BlogPostForm(instance=post)
        return render(request, "posts/post_form.html",{"form": form})
           
        
def search_posts(request): 
    query = request.GET['q'] 
    
    query_by_title = Q(title__contains=query)
    query_by_content = Q(content__contains=query)
    posts = Post.objects.filter(query_by_title | query_by_content)
    
    return render(request, "posts/posts_list.html", {'posts': posts})    
     
    