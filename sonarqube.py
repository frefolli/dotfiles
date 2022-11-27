#!/usr/bin/env python3
import json
import os
import shutil
import argparse
import sys

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

class Coverage:
    def launch(self):
        coverage = shutil.which("coverage")
        os.system(f"{coverage} run -m unittest discover")
        os.system(f"{coverage} report")
        os.system(f"{coverage} xml")

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
        self._setup_coverage()

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

    def _setup_coverage(self):
        coverage = self._get_secret("coverage")
        self._arguments.append(f"-Dsonar.python.coverage.reportPaths={coverage}")

    def launch(self):
        sonar_scanner = shutil.which("sonar-scanner")
        cmd = f"{sonar_scanner} {' '.join(self._arguments)}"
        os.system(cmd)

class Pipeline:
    def __init__(self, pipeline = None):
        if pipeline == None:
            pipeline = []
        self._pipeline = pipeline

    def append(self, tool):
        self._pipeline.append(tool)

    def launch(self):
        for tool in self._pipeline:
            tool.launch()

class CLI:
    def __init__(self):
        self._craft_parser()
        self._parse_args()
        self._craft_pipeline()

    def _craft_parser(self):
        self._parser = argparse.ArgumentParser(
                description = 'Sonarqube wrapper')

        self._parser.add_argument(
                '-S', '--no-sonarqube',
                default=False, action='store_true')
        
        self._parser.add_argument(
                '-C', '--no-coverage',
                default=False, action='store_true')
        
        self._parser.add_argument(
                '-p', '--secrets-path',
                default=".secrets", type=str, action='store')

    def _parse_args(self):
        self._config = self._parser.parse_args(sys.argv[1:])
    
    def _craft_pipeline(self):
        self._pipeline = Pipeline()
        if not self._config.no_coverage:
            self._pipeline.append(Coverage())
        if not self._config.no_sonarqube:
            self._pipeline.append(Sonarqube(SecretsFile(self._config.secrets_path)))

    def run(self):
        self._pipeline.launch()

if __name__ == "__main__":
    cli = CLI()
    cli.run()
