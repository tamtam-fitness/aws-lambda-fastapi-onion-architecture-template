# aws-lambda-fastapi-onion-architecture-template

This is a template for creating a FastAPI application with Onion Architecture and deploy it to AWS Lambda.

## project structure
this is a project structure image in app directory.
※ different from the actual project structure

```
├── api # presentation layer
│   ├── __init__.py
│   └── v1
│       ├── __init__.py
│       ├── endpoints
│       │   ├── __init__.py
│       │   └── <specific name>
│       └── router.py
├── compose.yml
├── container_config # DI container
│   ├── __init__.py
│   ├── di_container.py
│   └── module
│       ├── __init__.py
│       └── repository_module.py
├── core 
│   ├── __init__.py
│   ├── config.py
│   ├── logger
│   │   ├── __init__.py
│   │   ├── api_logger.py
│   │   └── logging_context_route.py
│   └── singleton.py
├── domain # domain layer
│   └── <specific name>
│       ├── service # business logic which is not written in entity and value object
│       ├── entity # mutable object
│       ├── i_repository # interface for repository(DIP)
│       └── value_object # immutable object
├── exceptions # custom exceptions
│   ├── core.py
│   ├── error_handle_middleware.py
│   └── error_messages.py
├── infrastructure # infrastructure layer
│    ├── repository_impl # implement repository interface
│    ├── model # ORM
├── main.py
├── schemas # DTO for using endpoint
├── scripts
│   └── compose_pytest
├── tests
├── usecase # application layer

```
If you want to separate command and query in domain layer, you can add CQRS pattern in usecase layer.

[this is a ariticle about CQRS pattern](https://iktakahiro.dev/python-ddd-onion-architecture#heading-cqrs-pattern).

## How to use
### 1. clone this repository
```bash
git clone
```

### 2. cd app directory
```bash
cd app
```

### 3. run container
run container following [app/README](app/README.md) .

## References

- [アプリケーションのレイヤ化](http://terasolunaorg.github.io/guideline/5.7.0.RELEASE/ja/Overview/ApplicationLayering.html)
- [ドメイン駆動設計のアーキテクチャ](https://little-hand-s.notion.site/8a666e49641248fa810ef382715cfe0f)
- [オニオンアーキテクチャを理解する](https://crane-techblog.com/onion-architecture/)
- [How to get started DDD & Onion-Architecture in Python web application](https://iktakahiro.dev/python-ddd-onion-architecture)
- [iktakahiro/dddpy](https://github.com/iktakahiro/dddpy)
- [tiangolo/full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [takashi-yoneya/fastapi-mybest-template](https://github.com/takashi-yoneya/fastapi-mybest-template)
