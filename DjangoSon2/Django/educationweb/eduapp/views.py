from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course
from teachers.models import Teacher
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from eduapp.models import Testimoniall, Contact
from . forms import ContactForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courselist'] = Course.objects.filter(available=True).order_by('-date')[:4]
        context['teachers'] = Teacher.objects.all()
        context['totol_course'] = Course.objects.filter(available=True).count()
        context['teacher_count'] = Teacher.objects.all().count()
        context['totol_students'] = User.objects.all().count()
        context['testimonials'] = Testimoniall.objects.all()
        # context['contacts'] = Contact.objects.all()

        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courselist'] = Course.objects.filter(available=True).order_by('-date')[:4]
        context['totol_course'] = Course.objects.filter(available=True).count()
        context['teacher_count'] = Teacher.objects.all().count()
        context['totol_students'] = User.objects.all().count()

        return context

class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Your request has been received.'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def testimonial(request):
    testimlist = Testimoniall.objects.all()
    stdcom = {
        'testimlist': testimlist
    }
    return render(request, 'testimonial.html', stdcom)

def feature(request):
    return render(request, "feature.html")

# def about(request):
#     return render(request, "about.html")

# from teachers.models import Teacher
# Create your views here.
