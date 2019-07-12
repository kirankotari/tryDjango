from django import forms
from allauth.account.forms import SignupForm
from .models import Location, Employee
from dashboard.models import Skills, Rating, EmployeeSkills
from django.db.utils import OperationalError


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)


class EmployeeSignupForm(SignupForm):
    locations = Location.objects.all()
    location_lst = []
    try:
        for l in locations:
            location_lst.append((l.location, l.location))
    except OperationalError:
        pass
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name', required=False)
    location = forms.ChoiceField(choices=location_lst)

    def save(self, request):
        u = super(EmployeeSignupForm, self).save(request)
        employee = Employee.objects.create(user=u, location=request.POST['location'])
        employee.save()

        skills = Skills.objects.all()
        rating = Rating.objects.filter(rate=0)[0]
        for each in skills:
            es = EmployeeSkills.objects.create(employee=u, skill=each, rating=rating)
            es.save()
        return u
