#!/usr/bin/env python
import os
import sys
import re

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    ######################################################
    # code from https://gist.github.com/bennylope/2999704
    # loads the variables defined in a local file .env
    if 'ON_HEROKU' not in os.environ: 
        try:
            with open('.env', 'r') as f:
                content = f.read()
        except IOError:
            print ('No .env file found.')
            content = ''
        for line in content.splitlines():
            m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
            if m1:
                key, val = m1.group(1), m1.group(2)
                m2 = re.match(r"\A'(.*)'\Z", val)
                if m2:
                    val = m2.group(1)
                m3 = re.match(r'\A"(.*)"\Z', val)
                if m3:
                    val = re.sub(r'\\(.)', r'\1', m3.group(1))
                os.environ.setdefault(key, val)
    ######################################################
    
    execute_from_command_line(sys.argv)
