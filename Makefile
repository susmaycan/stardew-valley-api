# ===================== MAKE SETTINGS ===================== #

.DEFAULT_GOAL := help
SHELL := /bin/bash
NAME := STARDEW VALLEY API

# ===================== HELP COLORS ===================== #

BOLD   := $(shell tput bold)
RED    := $(shell tput setaf 160)
ORANGE    := $(shell tput setaf 208)
GREEN  := $(shell tput setaf 2)
YELLOW := $(shell tput setaf 3)
BLUE   := $(shell tput setaf 45)
MAGENTA := $(shell tput setaf 98)
RESET  := $(shell tput sgr0)

# ===================== HELP COMMAND ===================== #

HELP := $(HELP),
HELP := $(HELP) $(BOLD)$(NAME) MAKE INTERFACE$(RESET),
HELP := $(HELP)   $(BOLD)$(RED)help$(RESET)                    Prints out this help message.,
HELP := $(HELP)   $(BOLD)$(ORANGE)build$(RESET)                   Builds project.,
HELP := $(HELP)   $(BOLD)$(YELLOW)run$(RESET)                     Runs project.,
HELP := $(HELP)   $(BOLD)$(GREEN)migrate_full$(RESET)            Runs Django migrations.,
HELP := $(HELP)   $(BOLD)$(BLUE)shell$(RESET)                   Opens bash terminal.,
HELP := $(HELP)   $(BOLD)$(MAGENTA)test$(RESET)                    Runs all the tests.,

.PHONY: help
help:
	@printf "$(HELP)" | tr , '\n'

DOCKER_COMPOSE_LOCAL=docker-compose.yml
SERVER_SERVICE=server
SERVER_CONTAINER=sv-server

# ===================== DOCKER COMMANDS ===================== #

.PHONY: run
run:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) up -d --remove-orphans

.PHONY: build
build:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) build

.PHONY: restart_api
restart_api:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) restart $(SERVER_SERVICE)

.PHONY: stop
stop:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) stop

.PHONY: down
down:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) down --volume

.PHONY: shell
shell:
	docker exec -ti $(SERVER_CONTAINER) bash

# ===================== DJANGO COMMANDS ===================== #
.PHONY: test
test:
	docker exec $(SERVER_CONTAINER) bash -c "python manage.py test"

.PHONY: makemigrations
makemigrations:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py makemigrations

.PHONY: migrate
migrate:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py migrate

.PHONY: migrate_full
migrate_full:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py makemigrations
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py migrate

.PHONY: load_data
load_data:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/season.json
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/rewards.json
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/bundle_room.json
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/bundles.json
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/bundle_items.json

.PHONY: dump_data
dump_data:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py dumpdata bundles.BundleItem > fixtures/bundle_item_dump.json

.PHONY: createsuperuser
createsuperuser:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py createsuperuser

.PHONY: check_linting
check_linting:
	docker exec $(SERVER_CONTAINER) bash -c "flake8"

.PHONY: fix_formatting
fix_formatting:
	docker exec $(SERVER_CONTAINER) bash -c "black ."
	docker exec $(SERVER_CONTAINER) bash -c "isort ."

.PHONY: generate_translations
generate_translations:
	docker exec $(SERVER_CONTAINER) bash -c "python manage.py makemessages -a"
