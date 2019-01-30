# Django - ITR

introtorhythm.com, but reimagined as a Django application! Hosted on an Ubuntu cloud server. ITR is a freeform podcast series featuring mixes and compositions from an international group of artists. Ocassionally, ITR serves as a live audio-streaming internet radio station (when we fell like it).

For information regarding:

* Dependencies
* AWS Storage
* Environment Variable Management
* Deployments
* SSL/ SSH

please [see the wiki](https://github.com/seanpierce/introtorhythm.com/wiki)!

### Local installation and usage

-   Clone this repo `$ git clone https://github.com/seanpierce/django-itr`
-   Install the dependencies that are listed above
-   From the project's root, run `$ python manage.py migrate` to generate the database
-   Create a config file for storing local environment variables `$ cd ../ && mkdir environment && touch environment/settings.ini`
	-   See `example_settings.ini` for implementation example
-   Back in the repo's root, start the Django development server by running `$ cd django-itr && python manage.py runserver`
-   Create an admin user by running `$ python manage.py createsuperuser` and follow the provided instructions
-   Visit <a href="http://localhost:8000/">localhost:8000</a> in your preferred browser

### Deployments

The application will be hosted on a DigitalOcean droplet cloud server running Ubuntu (16.04.5 x64). See Ubuntu setup documentation <a href="https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04">here</a>. The application is served using <a href="https://www.nginx.com/">Nginx</a> and <a href="https://gunicorn.org/">Gunicorn</a>. See webserver configuration documentation <a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04">here</a>.

After deploying code, or making updates on the server, restart nginx and gunicorn by running `sudo systemctl restart nginx gunicorn`

### SSL
Currently using a <a href="https://www.quora.com/What-is-Positive-SSL-and-how-is-it-implemented">positivessl</a> cert purchased/ managed through namecheap.
SSL cert was implemented via a combination of the following artices: <a href="https://simpleisbetterthancomplex.com/tutorial/2016/05/11/how-to-setup-ssl-certificate-on-nginx-for-django-application.html">Simple Cert</a> and <a href="https://www.digitalocean.com/community/tutorials/how-to-install-an-ssl-certificate-from-a-commercial-certificate-authority#install-certificate-on-web-server">Digitalocean install ssl cert instructions</a>. The cert expires in December 2019.

### TODOs
* Optimize code speed by performing fewer sql queries and serializing data less. See <a href="https://medium.com/@ryleysill93/basic-performance-optimization-in-django-ebd19089a33f">this article</a>.
* Implement async display of "live" feature, and implement async live chat using django-channels. See the docs <a href="https://channels.readthedocs.io/en/latest/">here</a>
