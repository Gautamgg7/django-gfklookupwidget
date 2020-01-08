dev-server: image-name := local/django-gfklookupwidget
dev-server:
	docker build --tag $(image-name) .
	docker run --interactive --tty --rm --publish 8000:8000 $(image-name)

pypi:
	docker run -it --rm -v $$(pwd):/workdir -w /workdir python:3.8.1-buster bash -c 'pip install twine; python setup.py sdist; twine upload dist/*'
