import pandas as pd
from django.contrib.auth.models import User
from .models import Skills, Rating, EmployeeSkills
from pages.models import Employee, Location


def load_skills():
    file_path = r'C:\Users\611776127\desktop\skill_metricx.xlsx'
    sheetname = 'Skills'
    df = pd.read_excel(file_path, sheet_name=sheetname)
    df_header = list(df)
    print(df_header)

    locations = set(df['Working Location'])
    print(locations)
    for each in locations:
        l = Location.objects.create(location=each)
        l.save()

    rating = set(df['Level'])
    for each in rating:
        if each.lower() != 'pending':
            r = Rating(rate=each.split()[0], title=each.split()[1])
            r.save()

    skills = df.drop_duplicates(subset=['Portfolio', 'Skills'], keep='first')
    for each in skills.itertuples(index=True, name="skill_pd"):
        s = Skills(portfolio=getattr(each, 'Portfolio'), tower=getattr(each, 'Tower'), technology=getattr(each, 'Technology'), skill_name=getattr(each, 'Skills'))
        s.save()

    users = df.drop_duplicates(subset='Name', keep='first')
    for each in users.itertuples(index=True, name="users_pd"):
        if pd.Series(getattr(each, '_3')).isnull()[0]:
            print('Not a valid user: {}'.format(getattr(each, 'Name')))
        else:
            u = User(username=str(getattr(each, '_3')).strip(), email=getattr(each, '_3'), first_name=getattr(each, 'Name'))
            u.set_password(getattr(each, 'EIN'))
            u.save()

            l = Location.objects.filter(location=getattr(each, '_5'))[0]
            e = Employee(user=u, location=l)
            e.save()

    for each in range(df['Skills'].count()):
        try:
            each_user = User.objects.filter(first_name=df['Name'][each])[0]
            each_skill = Skills.objects.filter(skill_name=df['Skills'][each], portfolio=df['Portfolio'][each])[0]
            try:
                rate, title = df['Level'][each].split()
                each_rating = Rating.objects.filter(rate=rate)[0]
            except ValueError as e:
                each_rating = Rating.objects.filter(rate=0)[0]
            es = EmployeeSkills(employee=each_user, skill=each_skill, rating=each_rating)
            es.save()
        except IndexError as e:
            print('Couldn\'t able to save Employee Skills {}'.format(df['Name'][each]))
            print(e)
        except Exception as e:
            print(e)


