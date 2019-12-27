# Project Exegol

Django application template for developing API using the Django Rest Framework.
Based on:

- `https://phalt.github.io/django-api-domains/`
- `https://github.com/HackSoftware/Django-Styleguide`

## Project structure

The application is organized around domains.
Every domain should contain:

- `api`
- `services`
- `models`
- `interfaces`

Every component can be a python file or package.

### API

We define API schema or every kind of presentation for the domain.

- APIs must be used as the entry point for all other consumers who wish to use this domain.
- APIs should own presentational logic and schema declarations.
- Internal domain-to-domain APIs should just be functions.
- You can group interal API functions under a class if it makes sense for organisation.
- If you are using a class for your internal APIs, it must use the naming convention MyDomainAPI.
- Internal functions in APIs must use type annotations.
- Internal functions in APIs must use keyword arguments.
- You should log API function calls.
- All data returned from APIs must be serializable.
- APIs must talk to Services to get data.
- APIs must not talk to Models directly.
- APIs should do simple logic like transforming data for the outside world, or taking external data and transforming it for the domain to understand.
- Objects represented through APIs do not have to map directly to internal database representations of data.

Additional ruling for DRF:

- You should serialize all models using DRF serializers.
- You should not use the ModelMixin Viewsets as they will tightly couple the data layer with the presentation layer.

### Services

We define logic around coordination and transactions.

- The primary components of Services should be functions.
- Services should own co-ordination and transactional logic.
- You can group functions under a class if it makes sense for organisation.
- If you are using a class, it must use the naming convention MyDomainService.
- Functions in services.py must use type annotations.
- Functions in services.py must use keyword arguments.
- You should be logging in services.py.

### Models

We define logic around the information.

- Models must not have any complex functional logic in them.
- Models should own informational logic related to them.
- Models can have computed properties where it makes sense.
- Models must not import services, interfaces, or apis from their own domain or other domains.
- Table dependencies (such as ForeignKeys) must not exist across domains. Use a UUID field instead, and have your Services control the relationship between models.
- You can use ForeignKeys between tables in one domain. (But be aware that this might hinder future refactoring.)

### Interfaces

We define logic for handling the transformation of data from other domains.

- The primary components of Interfaces should be functions.
- You can group functions under a class if it makes sense for organisation.
- If you are using a class, it must use the naming convention MyDomainInterface.
- Functions in Interfaces must use type annotations.
- Functions in Interfaces must use keyword arguments.

### Tests

The only place in your code that touches the outside world (anything outside your domain - other domains, or external consumers) is interfaces.py.
Any file that handles interfaces.py should mock out other dependent domains but you should still be testing your own interface definitions.
You should use Python's standard patch tool for this.
You can use MagicMock where it makes sense.
