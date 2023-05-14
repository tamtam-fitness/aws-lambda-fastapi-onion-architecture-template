## Run Container

To start development, you are supposed to run the following command:
```bash 
mutagen-compose build 

mutagen-compose up -d     
```

※ if you want to recreate image

if you want to see the api spec, you can access to `http://localhost:8080/docs`

## Development Commands

### enter into container
```bash
docker exec -it app bash
```

### intall
```bash 
make install
```

### lint

```bash 
make lint
```
### format

```bash 
make format
```

### test

if you want to run all tests, you can run the following command:
```bash 
make test
```

if you want to run the specific test, you can run the following command:
```bash
scripts/compose_pytest tests/{file or directory you want to test}
```
