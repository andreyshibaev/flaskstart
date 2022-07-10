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

    # if you want create or edit records in modal window
    create_modal = True
    edit_modal = True
    form_excluded_columns = ('confirmed_at', 'last_login_ip', 'last_login_at', 'current_login_at', 'current_login_ip', 'tf_primary_method', 'tf_totp_secret', 'tf_phone_number', 'us_totp_secrets', 'us_phone_number', 'login_count',)
    column_display_pk = True
    column_labels = {
        'id': 'id',
        'username': 'Имя пользователя',
        'email': 'Почта',
        'password': 'Пароль',
        'fs_uniquifier': 'Роль',
        'roles': 'Роли',
        'active': 'Активный',
    }

    column_list = ['id', 'username', 'email', 'roles']
    column_searchable_list = ['email', 'username']
    column_filters = ['email', 'username']

class RoleView(AccessCloseView, ModelView):
    column_display_pk = True

    column_choices = {
        'role': [
            ('role', 'name'),
        ]
    }

    column_labels = {
        'id': 'id',
        'name': 'Роль',
        'users': 'Пользователи',
        'description': 'Описание',
        'permissions': 'Разрешения',
          # 'update datetime': 'Дата обновления',
    }

    column_list = ['id', 'name',]
    column_searchable_list = ['name',]    