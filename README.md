Technologies : 
	- Django version 3.1.6
	- Python version 3.8.5

Deployment :
	From the terminal:
	1- Create virtual environment
		$ virtualenv venv
		
	2- Active the virtual environment
		$ source venv/bin/activate
		
	3- Upgrade pip
		$ pip install --upgrade pip

	4- Install the requirements modules
		$ pip install -r nls_world_map/requirements.txt
	
	5 - connect to server with FTP
	
	6- delete the file "index.html"
	
	7- Upload the folder "nls_world_map" content to the "WWW" or "WEB" direct in the server 
		
	8- In nls_world_map/nls_world_map/settings.py 
		a- Change the DATABASES configurations :
		
			from this configurations 
			
				DATABASES = {
				    'default': {
					'ENGINE': 'django.db.backends.sqlite3',
					'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
				    }
				}
				
			to this configurations
			
				DATABASES = {
				    'default': {
					'ENGINE': 'django.db.backends.mysql',
					'NAME': 'djangodatabase',
					'USER': 'dbadmin',
					'PASSWORD': '12345',
					'HOST': 'localhost',
					'PORT': '3306',
				    }
				}
				
		b- Change the SMTP EMAIL configurations
			EMAIL_BACKEND       = ""
			EMAIL_HOST          = ""
			EMAIL_PORT          = ""
			EMAIL_USE_TLS       = ""
			EMAIL_HOST_USER     = ""
			EMAIL_HOST_PASSWORD = ""
			
	
	9- Import data from the "db.sqlite3" file to Database
	
	..... AND THAT WILL WORK FINE .....
	
	Eyad
