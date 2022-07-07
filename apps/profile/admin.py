from flask_admin.contrib.sqla import ModelView
from flask import request, redirect, url_for
from flask_security import current_user
from flask_security import hash_password


class AccessCloseView():
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('admin')
        )
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class UserView(AccessCloseView, ModelView):
    def on_model_change(self, view, model, is_created):
        model.password = hash_password(model.password)

    column_display_pk = True
    column_labels = {
        'id': 'id',
        'username': 'Имя пользователя',
        'email': 'Почта',
        'password': 'Пароль',
        'fs_uniquifier': 'Роль',
        'roles': 'Роли',
        
    }

    column_list = ['id', 'username', 'email', 'roles']
    column_searchable_list = ['email', 'username']
    column_filters = ['email', 'username']

class RoleView(AccessCloseView, ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'id',
        'name': 'Роль',
        'users': 'Пользователи',
    }

    column_list = ['id', 'name',]
    column_searchable_list = ['name',]    