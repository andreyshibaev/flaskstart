from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'id',
        'username': 'Имя пользователя',
        'email': 'Почта',
        'password': 'Пароль',
        'fs_uniquifier': 'Роль',
    }

    column_list = ['id', 'username', 'email', 'roles']
    column_searchable_list = ['email', 'username']
    column_filters = ['email', 'username']

class RoleView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'id',
        'name': 'Роль',

    }
    column_list = ['id', 'name',]
    column_searchable_list = ['name',]    