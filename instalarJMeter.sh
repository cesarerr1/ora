#!/bin/bash

if ! command -v jmeter &> /dev/null; then
    echo "Jmeter no esta instalado"
    echo
    echo "Instalando jmeter..."

    wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.6.3.tgz

    tar xf apache-jmeter-5.6.3.tgz

    mv apache-jmeter-5.6.3 jmeter

    echo "sample_variables=response_body">>./jmeter/bin/jmeter.properties

    sudo mv jmeter /opt

    echo 'export PATH="$PATH:/opt/jmeter/bin"' >> ~/.bashrc
    source ~/.bashrc

    echo "Jmeter instalado correctamente"

    sudo rm apache-jmeter-5.6.3.tgz

else
    echo "Jmeter ya se encuentra instalado"
fi



