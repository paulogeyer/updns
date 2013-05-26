Dynamic DNS updater for afraid.org

it needs a config file in the ~/.updns

Example .updns file
[Router]
host=192.168.1.1
user=admin
pass=pass
[Config]
urls=[http://freedns.afraid.org/dynamic/update.php?yourcode,http://freedns.afraid.org/dynamic/update.php?anothercode]

after that, just add this script to your crontab