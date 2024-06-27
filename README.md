
# Django User Authenticator

A Django application for user registration and authentication, featuring Bootstrap-styled forms and custom form field validation.

## Features

- User Registration
- User Login
- Bootstrap-styled forms
- Custom validation messages

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fahad0samara/django-UserAuthenticator.git
    cd django-UserAuthenticator
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Open your browser and go to:**

    ```
    http://127.0.0.1:8000/
    ```

## Usage

### Register a New User

1. Navigate to the registration page.
2. Fill out the registration form and submit.

### Login

1. Navigate to the login page.
2. Enter your username and password and submit.

### Form Customization

The forms are styled using Bootstrap classes. You can customize the form fields and styles by modifying the `forms.py` and the corresponding templates.

**Example of `forms.py`:**

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
```

**Example of a registration template:**

```html
{% extends 'base.html' %}
{% block title %}Register - My Django App{% endblock %}

{% block content %}
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-body">
                    {% if form.errors %}
                        <div class="alert alert-danger" role="alert">
                            There was an error with your form.
                        </div>
                    {% endif %}

                    <h2 class="card-title text-center mb-4">REGISTER</h2>
                    <form method="POST" action="{% url 'register' %}">
                        {% csrf_token %}
                        <div class="form-row">
                            <div class="form-group col-md-6">
                                <label for="{{ form.username.id_for_label }}">Username:</label>
                                {{ form.username }}
                                {% if form.username.errors %}
                                    <div class="invalid-feedback d-block">
                                        {{ form.username.errors }}
                                    </div>
                                {% endif %}
                            </div>
                            <div class="form-group col-md-6">
                                <label for="{{ form.email.id_for_label }}">Email:</label>
                                {{ form.email }}
                                {% if form.email.errors %}
                                    <div class="invalid-feedback d-block">
                                        {{ form.email.errors }}
                                    </div>
                                {% endif %}
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group col-md-6">
                                <label for="{{ form.first_name.id_for_label }}">First Name:</label>
                                {{ form.first_name }}
                                {% if form.first_name.errors %}
                                    <div class="invalid-feedback d-block">
                                        {{ form.first_name.errors }}
                                    </div>
                                {% endif %}
                            </div>
                            <div class="form-group col-md-6">
                                <label for="{{ form.last_name.id_for_label }}">Last Name:</label>
                                {{ form.last_name }}
                                {% if form.last_name.errors %}
                                    <div class="invalid-feedback d-block">
                                        {{ form.last_name.errors }}
                                    </div>
                                {% endif %}
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group col-md-6">
                                <label for="{{ form.password1.id_for_label }}">Password:</label>
                                {{ form.password1 }}
                                {% if form.password1.errors %}
                                    <div class="invalid-feedback d-block">
                                        {{ form.password1.errors }}
                                    </div>
                                {% endif %}
                            </div>
                            <div class="form-group col-md-6">
                                <label for="{{ form.password2.id_for_label }}">Confirm Password:</label>
                                {{ form.password2 }}
                                {% if form.password2.errors %}
                                    <div class="invalid-feedback d-block">
                                        {{ form.password2.errors }}
                                    </div>
                                {% endif %}
                            </div>
                        </div>

                        {% if messages %}
                            {% for message in messages %}
                                <div class="alert alert-{{ message.tags }}">
                                    {{ message }}
                                </div>
                            {% endfor %}
                        {% endif %}

                        <button type="submit" class="btn btn-primary btn-block mt-4">Register</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

