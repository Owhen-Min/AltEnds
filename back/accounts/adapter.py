from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, commit=False)
        nickname = form.initial_data['nickname']
        first_name = form.initial_data['firstname']
        if nickname and first_name:
            user.nickname = nickname
            user.first_name = first_name
        user.save()
        return user