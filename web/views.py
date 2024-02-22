from django.shortcuts import render
from .models import Teachers, Blog, Contacts
from django.views.generic import TemplateView

from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
# def index(request):
class IndexView(TemplateView):
    template_name='web/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teach1"] = Teachers.objects.all()
        context["Blo"] = Blog.objects.all()

        return context
  
    
    
    
   
 


    
    
def Contact(request):
    if request.method == "POST":
        address = request.POST.get('address')
        name = request.POST.get('name')
        state = request.POST.get('state')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        contact2 = Contacts(
            address=address,
            name=name,
            state=state,
            email=email,
            mobile=mobile,
        )

        contact2.save()
        return redirect('seccess1/')
    
    return render(request, 'web/contact.html')
        
    




def seccess1_view(request):
    return render(request, 'web/Seccess.html')

    

  