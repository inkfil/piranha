
# piranha
an EDA tool in django


# EDA Tool (Django App)
Modules:
	1. Load CSV
	2. Preprocess
	3. Visualizing CSV Data
	4. Train Model
	5. Evaluate Model

### Load CSV
	* Upload CSV
	* custom delimiter
	* determine type of features
	* determine all posiible value that feature has
	* determine missing data
	* uploaded file name resolution

### Visualize CSV
	* type of plots
		- line plot
		- histogram
		- scatter plot
		- piechart/bargraph
		- box and whiskers (candle stick plot)
		- pair plots
		- violin plots
		- joint plots
		- 
		- 
	* features to visualize

### Preprocessing
	* fixing missing data
	* 


### Train Model


### requirements.txt
	* Numpy
	* Pandas
	* Scikit-Learn


### Django commands
	1. to create a django project
```bash
$ django-admin startproject EDA
```
	2. to create a django app
```bash
$ python3 manage.py startapp loadCSV
```
	3. adding app to project
	4. setting up routing
	5. creating a super user
	6. migrate and make migrate
	7. setting up models
	8. setting up forms
	9. setting up admin
	10. messages in django
	11. sessions in django
	12. cookies in django
	13. reset password in django
	14. setting up media and storage
	15. reverse_lazy (reverse name lookup)
	16. generic views, class views, function views


to run project
```bash
$ python3 manage.py runserver
```
 
to  make migrations to database
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

to check installed django version
```bash
$ python3 -m django --version
```
***


structure of a django app
__init__.py
admin.py
apps.py
forms.py
functions.py
models.py
urls.py
views.py

#settings.py (project)

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), ) 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#urls.py (project)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     # Project url patterns…
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


REFERENCES:
	https://ultimatedjango.com/


# D3.js
## CDN
```html
<!--D3js-->
<script type = "text/javascript" src="https://d3js.org/d3.v6.min.js"></script>
<!--Bootsrap-->
<!--jquery-->
<!--poper-->
<!--others-->
```

| Category | currency | sellerRating | Duration | endDay | ClosePrice | OpenPrice | Competitive |
| -------- | -------- | ------------ | -------- | ------ | ---------- | --------- | ----------- |
| Music/Movie/Game | US | 32495 | Mon | 0.01 | 0.01 | 0 |
| Music/Movie/Game | US | 32495 | Mon | 0.01 | 0.01 | 0 |
| Automotive | US | 31157 | Tue | 0.01 | 0.01 | 0 |
| Automotive | US | 31157 | Tue | 0.01 | 0.01 | 0 |
| Automotive | US | 31157 | Tue | 0.01 | 0.01 | 0 |
| Automotive | US | 31157 | Tue | 0.01 | 0.01 | 0 |
| Automotive | US | 31157 | Tue | 0.01 | 0.01 | 1 |
| Automotive | US | 31157 | Tue | 0.01 | 0.01 | 1 |




# How to setup django project in py3 virtual environment
```bash
$ pythom3 -m pip install django
$ python3 -m pip install virtualenv
$ mkdir ~/sample_venv
$ cd ~/sample_venv
$ virtualenv env_name
$ source env/bin/activate
$ python3 -m django --version
$ django-admin startproject EDA
$ python3 manage.py runserver

```
Machine Learning Life Cycle
- Data Collection

- Feature Engineering
	- Stats
	- Fix missing data
	- outlier detection and fixing
	- Standardization
	- Normalization
	- Data Augmentation
	- One Hot Encoding
	- Label Encoding
	- Feature Engineering
	- Feature Selection

- EDA
	- line plots
	- histogram
	- scatter plot
	- piechart/bargraph
	- box and whiskers (candle stick plot)
	- pair plots
	- violin plots
	- joint plots

- Model Selection
- Model Training
- Model Evaluation


REFERENCES:
	[CSV Header read only](https://stackoverflow.com/questions/24962908/how-can-i-read-only-the-header-column-of-a-csv-file-using-python)
	[looping pandas dataframe in django template](https://stackoverflow.com/questions/48762617/loop-pandas-table-in-django-template)
	
	
# Django Rest Framework (setup and samples)

## Installing Django and Django Rest Framework

```bash
sudo apt-get install python3 pip3
python3 -m pip installed django djangorestframework
```

## setting up django project

```bash
django-admin startproject <project-name>
```

```bash
cd <project-name>
python3 manage.py makemigrations
python3 manage.py migrate
python3 manaeg.py runserver
```

```
# Django Projec Structure

Root
├── Project
|  ├── __pycache__
|  ├── __init__.py
|  ├── asgi.py
|  ├── settings.py
|  ├── urls.py
|  └── wsgi.py
├── app1
|  ├── __pycache__
|  ├── migrations
|  ├── templates
|  ├── __init__.py
|  ├── admin.py
|  ├── apps.py
|  ├── functions.py
|  ├── models.py
|  ├── tests.py
|  ├── urls.py
|  └── views.py
├── app2
|  ├── __pycache__
|  └── ...
├── db.sqlite3
└── manage.py 
```

```bash
python3 manage.py startapp <app-name>
```

```python
# root/project/settings.py
INSTALLED_APPS=[
    ....,
    '<app-name>',
]
```

```python
# root/project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("<app-name>.urls")),
]
```

```python
# root/<app-name>/urls.py
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="basic_index")
]
```

```python
# root/<app-name>/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Fuck, world.")
```


