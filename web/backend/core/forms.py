from django import forms
from django.core.mail import EmailMessage
from django.conf import settings


class SupportForm(forms.Form):
    email = forms.EmailField(required=False)  # hidden field to detect SPAM
    reply = forms.EmailField(label="Reply to email", required=False)
    message = forms.CharField(
        widget=forms.Textarea, required=True, help_text="* Required"
    )

    def send_email(self, user, ip_addr, country_code):
        if self.cleaned_data["email"]:
            # SPAM
            return

        if self.cleaned_data["reply"]:
            reply = self.cleaned_data["reply"]
        else:
            if user.first_name or user.last_name:
                reply = "%s %s <%s>" % (
                    user.first_name or "",
                    user.last_name or "",
                    user.email,
                )
            else:
                reply = "%s <%s>" % (user.username, user.email)

        header = (
            "From: {email}\n" "IP Country: {country}\n" "IP: {ip}\n"
        ).format(email=reply, ip=ip_addr, country=country_code)

        msg = EmailMessage(
            "Support Form Request",
            header + "\n\n%s" % self.cleaned_data["message"],
            settings.DEFAULT_FROM_EMAIL,
            [settings.SUPPORT_EMAIL],
            reply_to=[reply],
        )
        msg.send(fail_silently=False)
