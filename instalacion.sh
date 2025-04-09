#!/bin/bash

log_file="installation_log.txt"
system_log_path="/usr/local/"

# Eliminar el archivo de registro existente si existe
rm -f "$log_file"

echo "------Registro de instalación y ejecución------" | tee -a "$log_file"
echo 
echo 

chmod +x ./instalarJavaJDK.sh
echo "------Realizando la instalación de Java JDK------" | tee -a "$log_file"
./instalarJavaJDK.sh | tee -a "$log_file" 2>&1

chmod +x ./instalarAllure.sh
echo "------Instalando Allure------" | tee -a "$log_file"
./instalarAllure.sh | tee -a "$log_file" 2>&1

chmod +x ./instalarVirtualenv.sh
echo "------Instalando Pipenv mediante PIP------" | tee -a "$log_file"
./instalarVirtualenv.sh | tee -a "$log_file" 2>&1

chmod +x ./instalarSDKAndroid.sh
echo "------Instalando SDK ------" | tee -a "$log_file"
./instalarSDKAndroid.sh | tee -a "$log_file" 2>&1

chmod +x ./instalarADB.sh
echo "------Instalando ADB ------" | tee -a "$log_file"
./instalarADB.sh | tee -a "$log_file" 2>&1

chmod +x ./appiumServer.sh
echo "------Instalando Appium server ------" | tee -a "$log_file"
./appiumServer.sh | tee -a "$log_file" 2>&1

chmod +x ./instalarJMeter.sh
chmod +x ./inicio.sh
chmod +x ./web.sh
chmod +x ./desktop.sh
chmod +x ./iniciarAppium.sh
chmod +x ./obtenerDispositivos.sh
chmod +x ./movil.sh


sudo cp -f "$log_file" "$system_log_path$log_file"
