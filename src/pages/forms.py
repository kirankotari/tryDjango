from django import forms
from allauth.account.forms import SignupForm
from .models import Location, Employee


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)


class EmployeeSignupForm(SignupForm):
    locations = Location.objects.all()
    location_lst = []
    for l in locations:
        location_lst.append((l.location, l.location))

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name', required=False)
    location = forms.ChoiceField(choices=location_lst)

    def save(self, request):
        u = super(EmployeeSignupForm, self).save(request)
        employee = Employee.objects.create(user=u, location=request.POST['location'])
        employee.save()
        return u
