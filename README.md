# Django - ITR

introtorhythm.com, but reimagined as a Django application!

### Dependencies

Install the following using `pip install`

-   django (duh!)
-   django-storages
-   boto3
-   djangorestframework
-   Pillow (for ImageField/ FileField access in models)

### Local installation and usage

-   Clone this repo by running `$ git clone https://github.com/seanpierce/django-itr`
-   Rename `django-itr/_secrets.py` to `django-itr/secrets.py` and add your <a href="https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html">AWS security credentials</a>
-   Install the dependencies that are listed above
-   From the project's root, run `$ python manage.py migrate` to generate the database
-   Start the Django development server by running `$ python manage.py runserver 0.0.0.0:8000`
-   Create an admin user by running `$ python manage.py createsuperuser` and follow the provided instructions
-   Visit <a href="http://localhost:8000/">localhost:8000</a> in your preferred browser

### AWS storage

Admin-uploaded files are stored in an AWS S3 bucket. This functionality is possible using **boto3** and **django-storages** installed via pip.
See implementation docs <a href="https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html">here</a>.

### REST API

An integrated REST API is implemented using **djangorestframework** installed viia pip. See implementation docs <a href="https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5">here</a>.

### Deployments

The application will be hosted on an Elastic Beanstalk instance and deployments will be handled using AWS's `awsebcli` command-line tools. See implementation docs <a href="https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html">here</a>.

Currently exposed routes:

| Method |   Endpoint    |             Result             |
| :----: | :-----------: | :----------------------------: |
|  GET   | /api/episodes | All episode numbers and titles |
