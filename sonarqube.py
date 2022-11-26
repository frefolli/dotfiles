#!/usr/bin/env python3
import json
import os
import shutil

class SecretsDictionary:
    def __init__(self, secrets = None):
        if secrets == None:
            secrets = {}
        self._secrets = secrets

    def get_secret(self, *keys):
        secrets = self._secrets
        for key_index in range(len(keys)):
            key = keys[key_index]
            if key not in secrets:
                key_path = '.'.join(keys[:key_index+1])
                raise Exception(f"{key_path} not in secrets")
            secrets = secrets[key]
        return secrets

class SecretsFile:
    def __init__(self, filepath = None):
        if filepath == None:
            filepath = ".secrets"
        self._filepath = filepath
        self._read_secrets()

    def _read_secrets(self):
        with open(self._filepath) as secrets_file:
            self._secrets = SecretsDictionary(json.loads(secrets_file.read()))

    def get_secret(self, *keys):
        return self._secrets.get_secret(*keys)

class Sonarqube:
    def __init__(self, secrets = None):
        if secrets == None:
            secrets = SecretsFile()
        self._secrets = secrets
        self._setup()

    def _get_secret(self, *keys):
        return self._secrets.get_secret("sonarqube", *keys)

    def _setup(self):
        self._arguments = []
        self._setup_login()
        self._setup_host_url()
        self._setup_project_key()
        self._setup_sources()

    def _setup_login(self):
        login = self._get_secret("access_token")
        self._arguments.append(f"-Dsonar.login={login}")
    
    def _setup_host_url(self):
        host_url = self._get_secret("server_url")
        self._arguments.append(f"-Dsonar.host.url={host_url}")
    
    def _setup_project_key(self):
        project_key = self._get_secret("project_key")
        self._arguments.append(f"-Dsonar.projectKey={project_key}")
    
    def _setup_sources(self):
        sources = self._get_secret("sources")
        self._arguments.append(f"-Dsonar.sources={sources}")

    def launch(self):
        sonar_scanner = shutil.which("sonar-scanner")
        os.execv(sonar_scanner, self._arguments)

if __name__ == "__main__":
    sonarqube = Sonarqube()
    sonarqube.launch()
