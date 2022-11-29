# config
My config files

 - .emacs
 - .vimrc
 - .bashrc

# Development

## Secrets File

Composition of `.secrets` file is very simple

```json
{
    "sonarqube": {
        "access_token": "<ACCESS_TOKEN>",
        "server_url": "<SERVER_URL>",
        "project_key": "<PROJECT_KEY>",
        "sources": "<SOURCES>",
        "coverage": "<COVERAGE_XML>",
        "python_version": "<PYTHON_VERSION>"

    }
}
```

## Architectural & Design Patterns

| file | component | pattern | description |
| --- | --- | --- | --- |
| src/context.py | Context | Lazy Load | singleton for `Context._repository` |

