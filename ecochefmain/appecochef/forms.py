from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class IngredientsForm(forms.Form):
    ingredients = forms.CharField(widget=forms.Textarea, help_text="Enter ingredients separated by commas.")

class CuisineForm(forms.Form):
    cuisine = forms.ChoiceField(choices=[('French', 'French'), ('Japanese', 'Japanese'), ('Indo-Chinese', 'Indo-Chinese')], required=True)
    meal = forms.ChoiceField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack'), ('drink', 'Drink')], required=True)
    time = forms.IntegerField(help_text="Time in minutes")

class PreferencesForm(forms.Form):
    spice_level = forms.ChoiceField(choices=[('no spice', 'No Spice'), ('mild', 'Mild'), ('medium', 'Medium'), ('hot', 'Hot'), ('extra hot', 'Extra Hot'), ('any', 'Any')], required=True)
    dietary_preferences = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter any dietary preferences.")
    allergies = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter any allergies.")

class NutritionalForm(forms.Form):
    calories = forms.IntegerField(required=False)
    carbs = forms.IntegerField(required=False)
    fat = forms.IntegerField(required=False)
    protein = forms.IntegerField(required=False)
