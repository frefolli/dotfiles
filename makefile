@all:
	@ echo "call make install"

sonarqube:
	@ ./sonarqube.py

install:
	@ ./dpcm -h

clean:
	@ ./clean.sh
