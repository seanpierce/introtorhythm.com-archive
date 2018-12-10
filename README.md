# Django - ITR

introtorhythm.com, but reimagined as a Django application!

### AWS storage
Admin-uploaded files are stored in an AWS S3 bucket. This functionality is possible using **boto3** and **django-storages** installed via pip.
See implementation docs <a href="https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html">here</a>.

### REST API
An integrated REST API is implemented using **djangorestframework** installed viia pip. See implementation docs <a href="https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5">here</a>.

Currently exposed routes:

| Method | Endpoint | Result |
|:---:|:---:|:---:|
| GET | /api/episodes| All episode numbers and titles |