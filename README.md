![](https://user-images.githubusercontent.com/15679739/51988581-3967a700-2462-11e9-8ef3-c73ab80540b7.png)

# introtorhythm.com

introtorhythm.com, but reimagined as a Django application! Hosted on an Ubuntu cloud server. ITR is a freeform podcast series featuring mixes and compositions from an international group of artists. Ocassionally, ITR serves as a live audio-streaming internet radio station (when we fell like it).

Additionally, ITR is dedicated to open-source projects, and the collective idea sharing that fuels creative expression. If you're interested in developing your own live-streaming station or podcasting platform, you're invited to refer to ITR's source code here, or ask questions by sending a message to introtorhythm@gmail.com

For information regarding:

* Live-Streaming
* Dependencies
* AWS Storage
* Environment Variable Management
* Deployments
* SSL/ SSH

please [see the wiki](https://github.com/seanpierce/introtorhythm.com/wiki)!

### Local installation and usage

-   Clone this repo `$ git clone https://github.com/seanpierce/django-itr`
-   Install the [dependencies](https://github.com/seanpierce/introtorhythm.com/wiki/Dependencies)
-   From the project's root, run `$ python manage.py migrate` to generate the database
-   Create a config file for storing local [environment variables](https://github.com/seanpierce/introtorhythm.com/wiki/Environment-Variables) `$ cd ../ && mkdir environment && touch environment/settings.ini`
	-   See `example_settings.ini` for implementation example
-   Back in the repo's root, start the Django development server by running `$ cd django-itr && python manage.py runserver`
-   Create an admin user by running `$ python manage.py createsuperuser` and follow the provided instructions
-   Visit <a href="http://localhost:8000/">localhost:8000</a> in your preferred browser

### License
* [MIT](https://raw.githubusercontent.com/seanpierce/introtorhythm.com/master/LICENSE)
