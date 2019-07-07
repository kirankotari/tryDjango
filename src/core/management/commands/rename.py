from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('old_project_name', type=str, help='The current Django project name')
        parser.add_argument('new_project_name', type=str, help='The new Django project name')
        # parser.add_argument('-p', '--prefix')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']
        old_project_name = kwargs['old_project_name']

        # bit of logic to rename the project

        files_to_rename = ['{}/settings/base.py'.format(old_project_name),
                           '{}/wsgi.py'.format(old_project_name),
                           'manage.py']
        folders_to_rename = old_project_name

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(old_project_name, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folders_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been rename to {}'.format(new_project_name)))

