# Django Template

A basic starting point for a Django app. Intentionally simple and opinionated. Strongly influenced by the original [Two Scoops of Django template](https://github.com/twoscoops/django-twoscoops-project) and its latest iteration [`cookiecutter-django`](https://github.com/pydanny/cookiecutter-django).

## Requirements

- Django 1.9
- Node.js
- `virtualenvwrapper`
- Willingness to change this README to something that makes sense with your project post-generation

## Getting started

Please note – this guide assumes you are using OS X.

First, create the folder for you project.

```bash
mkdir <folder-of-your-project>
```

Then, create the virtual environment for your project.

```bash
mkvirtualenv <name-of-your-project>-dev
```

Next, install Django.

```bash
pip install django
```

Now we're ready to pull in the template. Take note &mdash; if you do not pass in the `<folder-of-your-project>`, it'll create a new one for you.

```bash
django-admin startproject --template=https://github.com/rdmurphy/django-template/archive/master.zip --extension=coveragerc,gitignore,html,py,js,sh <name-of-your-project> <folder-of-your-project>
```

Jump into your newly created project folder, get `git` initialized, and make your first commit.

```bash
cd <folder-of-your-project>
git init
git add .
git commit -m "Initial commit"
```

Now, install your local development requirements.

```bash
pip install -r requirements/local.txt
```

You should be able to run your first `migrate` now! Give it a try.

```bash
python <name-of-your-project>/manage.py migrate
```

Next, we'll install the Node.js dependencies for building our static assets.

```bash
npm install
```

Then we can build our assets.

```bash
npm run build/production
```

The assets can auto-compile while you work, too!

```bash
npm run serve
```

And it should be able to handle `runserver` now, too.

```bash
python <name-of-your-project>/manage.py runserver
```

If everything checks out you're good to go. Don't forget to replace this README!
