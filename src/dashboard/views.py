from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from collections import OrderedDict
from .models import EmployeeSkills, Rating, Skills


@login_required
def dashboard(request, *args, **kwargs):
    template = 'dashboard.html'
    # print(request.user)

    if request.method == "POST":
        es = EmployeeSkills.objects.filter(employee=request.user)
        for each_es in es:
            skill = Skills.objects.filter(skill_name=each_es.skill.skill_name)
            rating = Rating.objects.filter(rate=request.POST.get(each_es.skill.skill_name.replace(' ', '_')))
            EmployeeSkills.objects.filter(skill=skill[0]).update(rating=rating[0])

    treeView = OrderedDict()
    r = Rating.objects.all()
    es = EmployeeSkills.objects.filter(employee=request.user)
    for each_es in es:
        if each_es.skill.portfolio not in treeView:
            treeView = {each_es.skill.portfolio: {each_es.skill.tower: {each_es.skill.technology: {each_es.skill.skill_name: each_es.rating}}}}
        elif each_es.skill.tower not in treeView[each_es.skill.portfolio]:
            treeView[each_es.skill.portfolio][each_es.skill.tower] = {each_es.skill.technology: {each_es.skill.skill_name: each_es.rating}}
        elif each_es.skill.technology not in treeView[each_es.skill.portfolio][each_es.skill.tower]:
            treeView[each_es.skill.portfolio][each_es.skill.tower][each_es.skill.technology] = {each_es.skill.skill_name: each_es.rating}
        else:
            treeView[each_es.skill.portfolio][each_es.skill.tower][each_es.skill.technology][each_es.skill.skill_name] = each_es.rating
    try:
        context = {'employee': es[0].employee, 'treeView': treeView, 'n': r}
    except Exception:
        context = {}

    # from .import_skills import load_skills
    # load_skills()
    return render(request, template, context)


