
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
<script type = "text/javascript" src="https://d3js.org/d3.v6.min.js"></script>
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
$ django-admin startproject EDA
$ python3 manage.py runserver

```