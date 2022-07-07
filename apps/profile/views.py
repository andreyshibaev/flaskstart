from flask import Blueprint, request, url_for, redirect, render_template

profile = Blueprint('profile', __name__, template_folder="templates/profile")


from flask_security import auth_required
@profile.route("/profile")
@auth_required()
def profile_account():
    return render_template('profile.html')



from flask_admin import AdminIndexView
from flask_security import current_user
class AdminView(AdminIndexView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('admin')
        )
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url)) 
