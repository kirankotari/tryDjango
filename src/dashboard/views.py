from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from collections import OrderedDict
from .models import EmployeeSkills, Rating, Skills


@login_required
def dashboard(request, *args, **kwargs):
    template = 'dashboard.html'
    # print(request.user)

    es = EmployeeSkills.objects.filter(employee=request.user)
    treeView = OrderedDict()
    rating_dict = {'0':'0 -> None', '1':'1 -> Basic', '2':'2 -> Intermediate', '3':'3 -> Full', '4':'4 -> Expert'}
    for each_es in es:
        if request.method == 'POST':
            skill = Skills.objects.filter(skill_name=each_es.skill.skill_name)
            rating = Rating.objects.filter(rate=request.POST.get(each_es.skill.skill_name.replace(' ', '_'))[0])
            EmployeeSkills.objects.filter(skill=skill[0]).update(rating=rating[0])

        if each_es.skill.portfolio not in treeView:
            treeView = {each_es.skill.portfolio: {each_es.skill.tower: {each_es.skill.technology: {each_es.skill.skill_name: each_es.rating.rate}}}}
        elif each_es.skill.tower not in treeView[each_es.skill.portfolio]:
            treeView[each_es.skill.portfolio][each_es.skill.tower] = {each_es.skill.technology: {each_es.skill.skill_name: each_es.rating.rate}}
        elif each_es.skill.technology not in treeView[each_es.skill.portfolio][each_es.skill.tower]:
            if request.method == 'POST':
                treeView[each_es.skill.portfolio][each_es.skill.tower][each_es.skill.technology] = {each_es.skill.skill_name: rating_dict[request.POST.get(each_es.skill.skill_name.replace(' ', '_'))[0]]}
            else:
                treeView[each_es.skill.portfolio][each_es.skill.tower][each_es.skill.technology] = {each_es.skill.skill_name: rating_dict[each_es.rating.rate]}
        else:
            if request.method == 'POST':
                treeView[each_es.skill.portfolio][each_es.skill.tower][each_es.skill.technology][each_es.skill.skill_name] = rating_dict[request.POST.get(each_es.skill.skill_name.replace(' ', '_'))[0]]
            else:
                treeView[each_es.skill.portfolio][each_es.skill.tower][each_es.skill.technology][each_es.skill.skill_name] = rating_dict[each_es.rating.rate]
    try:
        print(treeView)
        context = {'employee': es[0].employee, 'treeView': treeView, 'n': ['0 -> None', '1 -> Basic', '2 -> Intermediate', '3 -> Full', '4 -> Expert']}
    except Exception:
        context = {}
    return render(request, template, context)


