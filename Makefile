pypi:
	docker run -it --rm -v $$(pwd):/workdir -w /workdir python bash -c 'pip install twine; python setup.py sdist; twine upload dist/*'
