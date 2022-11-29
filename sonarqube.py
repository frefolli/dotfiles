#!/usr/bin/env python3
import json
import os
import shutil
import argparse
import sys

class Distro:
    def get_coverage(self):
        raise Exception("template method")

    def get_sonar_scanner(self): 
        raise Exception("template method")

class DebianLinux:
    def get_coverage(self):
        coverage = shutil.which("python3-coverage")
        if not coverage:
            raise ValueError("python3 coverage not found")
        return coverage
    
    def get_sonar_scanner(self): 
        sonar_scanner = shutil.which("sonar-scanner")
        if not sonar_scanner:
            raise ValueError("sonar-scanner not found")
        return sonar_scanner

class UbuntuLinux:
    def get_coverage(self):
        coverage = shutil.which("python3-coverage")
        if not coverage:
            raise ValueError("python3 coverage not found")
        return coverage
    
    def get_sonar_scanner(self): 
        sonar_scanner = shutil.which("sonar-scanner")
        if not sonar_scanner:
            raise ValueError("sonar-scanner not found")
        return sonar_scanner

class ArchLinux:
    def get_coverage(self):
        coverage = shutil.which("coverage")
        if not coverage:
            raise ValueError("python3 coverage not found")
        return coverage
    
    def get_sonar_scanner(self): 
        sonar_scanner = shutil.which("sonar-scanner")
        if not sonar_scanner:
            raise ValueError("sonar-scanner not found")
        return sonar_scanner

class DistroFactory:
    @staticmethod
    def get_distro():
        with open("/etc/issue", "r") as issue_file:
            issue = issue_file.read()
            if "Debian" in issue:
                return DebianLinux()
            if "Ubuntu" in issue:
                return UbuntuLinux()
            elif "Arch" in issue:
                return ArchLinux()
            else:
                raise ValueError("wrong distro")

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
    def __init__(self):
        self._setup()

    def _setup(self):
        self._setup_command()

    def _setup_command(self):
        distro = DistroFactory.get_distro()
        self._coverage = distro.get_coverage()
        
    def launch(self):
        os.system(f"{self._coverage} run --source=installer -m unittest discover")
        os.system(f"{self._coverage} report")
        os.system(f"{self._coverage} xml")
        os.system(f"{self._coverage} html")

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
        self._setup_command()
        self._setup_login()
        self._setup_host_url()
        self._setup_project_key()
        self._setup_sources()
        self._setup_coverage()
        self._setup_python_version()

    def _setup_command(self):
        distro = DistroFactory.get_distro()
        self._sonar_scanner = distro.get_sonar_scanner()

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

    def _setup_python_version(self):
        python_version = self._get_secret("python_version")
        self._arguments.append(f"-Dsonar.python.version={python_version}")

    def launch(self):
        cmd = f"{self._sonar_scanner} {' '.join(self._arguments)}"
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
