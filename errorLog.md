### 1. ERROR: password fields do not render in django forms
#### SOL: `password1` and `password2` are "custom" fields on the `UserCreationForm` since they do not exist as model fields on the `User` model. `Meta.widgets` will not work for these custom fields, you will need to redefine these fields and their widgets in your form

 ``` 
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter password'}),
    )
```

### 2. ERROR: SMTPAuthenticationError at /register/
> (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials b9-20020a170902d50900b0016a1e2d148csm2935141plg.32 - gsmtp')

#### SOL: solved it with resetting the os environment variables, the values shouldn't be enclosed in quotes. For example, MAIL_USERNAME=blah@gmail.com.