from distutils.core import setup

setup(
    name='django-gfklookupwidget',
    version='1.0.8',
    description=(
        'A widget to replace the object_id in a generic relation with a '
        'search link.'
    ),
    long_description=(
        'A widget to replace the object_id in a generic relation with a '
        'search link. It will open a popup to select a related item based on '
        'the content_type field. It supports inlines.'
    ),
    keywords='django, contenttype, genericforeignkey, generic, relation',
    author='Mason Staugler',
    author_email='mason@staugler.net',
    url='https://github.com/mqsoh/django-gfklookupwidget',
    packages=['gfklookupwidget'],
    license='ISC license',
)
