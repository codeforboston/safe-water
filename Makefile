.PHONY: serve build push

all: serve

serve:
	docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material

build:
	docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material build

deploy: build
	docker run --rm -it -v ~/.ssh:/root/.ssh -v ${PWD}:/docs squidfunk/mkdocs-material gh-deploy 
