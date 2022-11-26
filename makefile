@all:
	@ echo "call make install"

sonarqube:
	@ ./sonarqube.py

install:
	@ ./install.py

clean:
	@ ./clean.sh
