#!/bin/bash

# Obtener el valor de $project_name pasado como argumento
project_name="$1"

"$PWD/instalarNodeJs.sh"
"$PWD/instalarNewmanAndReporters.sh"

cd "$project_name" || exit
cd servicios
mkdir -p postman

cd postman

echo "Instalando dependencias, espere por favor..."




# Ejecutar los comandos y redirigir la salida para que no sea visible
{
    pip install behave 
    pip install allure-behave
} > /dev/null 2>&1


echo "Entorno virtual creado satisfactoriamente"
echo 


###############################################################################
# Crear estrutura de carpetas del proyecto

cat > ./behave.ini<<END
[behave]
format = allure_behave.formatter:AllureFormatter
outfiles = allure-results
END

mkdir -p colection

cat > colection/postman_collection.json<<END
{
	"info": {
		"_postman_id": "77e47132-35d5-49b9-bc13-c18f6f37af22",
		"name": "TestApi",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "24892036"
	},
	"item": [
		{
			"name": "ClimaXalapa",
			"event": [
				{
					"listen": "test",
					"script": {
						"exec": [
							"pm.test(\"Latitud correcta\", function () {\r",
							"    const responseData = pm.response.json();\r",
							"\r",
							"    latitud = pm.variables.get(\"latitud\");\r",
							"    pm.expect(responseData.coord.lat).to.eql(latitud);\r",
							"});\r",
							"\r",
							"pm.test(\"Longitu correcta\", function () {\r",
							"    const responseData = pm.response.json();\r",
							"\r",
							"    longitud = pm.variables.get(\"longitud\");\r",
							"    pm.expect(responseData.coord.lon).to.eql(longitud);\r",
							"});\r",
							"\r",
							"pm.test(\"El país es MX\", function () {\r",
							"    pais = pm.collectionVariables.get(\"pais\")\r",
							"    pm.expect(pm.response.json().sys.country).to.eql(pais);\r",
							"});\r",
							"\r",
							"pm.test(\"La ciudad es Xalapa\", function () {\r",
							"    ciudad = pm.collectionVariables.get(\"ciudad\")\r",
							"    pm.expect(pm.response.json().name).to.eql(ciudad);\r",
							"});\r",
							"\r",
							"\r",
							"pm.test(\"Codigo de respuesta es 200\", function () {\r",
							"  pm.response.to.have.status(200);\r",
							"});\r",
							"\r",
							"\r",
							"\r",
							"pm.test(\"Validar la estructura del JSON de respuesta\", function () {\r",
							"    const responseData = pm.response.json();\r",
							"    \r",
							"    pm.expect(responseData).to.have.property('coord');\r",
							"    pm.expect(responseData).to.have.property('weather');\r",
							"    pm.expect(responseData).to.have.property('base');\r",
							"    pm.expect(responseData).to.have.property('main');\r",
							"    pm.expect(responseData).to.have.property('visibility');\r",
							"    pm.expect(responseData).to.have.property('wind');\r",
							"    pm.expect(responseData).to.have.property('clouds');\r",
							"    pm.expect(responseData).to.have.property('dt');\r",
							"    pm.expect(responseData).to.have.property('sys');\r",
							"    pm.expect(responseData).to.have.property('timezone');\r",
							"    pm.expect(responseData).to.have.property('id');\r",
							"    pm.expect(responseData).to.have.property('name');\r",
							"    pm.expect(responseData).to.have.property('cod');\r",
							"});\r",
							"\r",
							"\r",
							"pm.test(\"Los campos obligatorios estan presentes en la respuesta\", function () {\r",
							"    const responseData = pm.response.json();\r",
							"    \r",
							"    pm.expect(responseData).to.be.an('object');\r",
							"    pm.expect(responseData.coord).to.exist;\r",
							"    pm.expect(responseData.weather).to.exist;\r",
							"    pm.expect(responseData.base).to.exist;\r",
							"    pm.expect(responseData.main).to.exist;\r",
							"    pm.expect(responseData.visibility).to.exist;\r",
							"    pm.expect(responseData.wind).to.exist;\r",
							"    pm.expect(responseData.clouds).to.exist;\r",
							"    pm.expect(responseData.dt).to.exist;\r",
							"    pm.expect(responseData.sys).to.exist;\r",
							"    pm.expect(responseData.timezone).to.exist;\r",
							"    pm.expect(responseData.id).to.exist;\r",
							"    pm.expect(responseData.name).to.exist;\r",
							"    pm.expect(responseData.cod).to.exist;\r",
							"});\r",
							"\r",
							"\r",
							"pm.test(\"la fecha en la respuesta tienen el formato correcto\", function () {\r",
							"    const responseData = pm.response.json();\r",
							"    \r",
							"    pm.expect(responseData).to.be.an('object');\r",
							"    pm.expect(responseData.dt).to.be.a('number');\r",
							"    pm.expect(responseData.sys.sunrise).to.be.a('number');\r",
							"    pm.expect(responseData.sys.sunset).to.be.a('number');\r",
							"});\r",
							"\r",
							"\r",
							"///////////////////////////////////////////////////////////////\r",
							"///////////////////////////////////////////////////////////////\r",
							"///////////////////////////////////////////////////////////////\r",
							"pm.test(\"El header 'Content-Type' es correcto\", function () {\r",
							"    pm.expect(pm.response.headers.get('Content-Type')).to.eql('application/json; charset=utf-8');\r",
							"});\r",
							"\r",
							"pm.test(\"El header 'Content-Length' es correcto\", function () {\r",
							"    pm.expect(pm.response.headers.get('Content-Length')).to.eql('504');\r",
							"});\r",
							"\r",
							"pm.test(\"El header 'Connection' es correcto\", function () {\r",
							"    pm.expect(pm.response.headers.get('Connection')).to.eql('keep-alive');\r",
							"});\r",
							"\r",
							"pm.test(\"El header 'Access-Control-Allow-Origin' es correcto\", function () {\r",
							"    pm.expect(pm.response.headers.get('Access-Control-Allow-Origin')).to.eql('*');\r",
							"});\r",
							"\r",
							"pm.test(\"El header 'Access-Control-Allow-Credentials' es correcto\", function () {\r",
							"    pm.expect(pm.response.headers.get('Access-Control-Allow-Credentials')).to.eql('true');\r",
							"});\r",
							"\r",
							"pm.test(\"El header 'Access-Control-Allow-Methods' es correcto\", function () {\r",
							"    pm.expect(pm.response.headers.get('Access-Control-Allow-Methods')).to.eql('GET, POST');\r",
							"});\r",
							""
						],
						"type": "text/javascript",
						"packages": {}
					}
				},
				{
					"listen": "prerequest",
					"script": {
						"exec": [
							"pm.collectionVariables.set(\"latitud\", 19.5312);\r",
							"pm.collectionVariables.set(\"longitud\", -96.9159);\r",
							"pm.collectionVariables.set(\"apikey\",'d26edded5926f6d4b891d67d05a84eb2');\r",
							"pm.collectionVariables.set(\"pais\", \"MX\");\r",
							"pm.collectionVariables.set(\"ciudad\", \"Xalapa\");\r",
							""
						],
						"type": "text/javascript",
						"packages": {}
					}
				}
			],
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "https://api.openweathermap.org/data/2.5/weather?lat={{latitud}}&lon={{longitud}}&appid={{apikey}}",
					"protocol": "https",
					"host": [
						"api",
						"openweathermap",
						"org"
					],
					"path": [
						"data",
						"2.5",
						"weather"
					],
					"query": [
						{
							"key": "lat",
							"value": "{{latitud}}"
						},
						{
							"key": "lon",
							"value": "{{longitud}}"
						},
						{
							"key": "appid",
							"value": "{{apikey}}"
						}
					]
				}
			},
			"response": []
		}
	],
	"variable": [
		{
			"key": "latitud",
			"value": ""
		},
		{
			"key": "longitud",
			"value": ""
		},
		{
			"key": "apikey",
			"value": ""
		},
		{
			"key": "pais",
			"value": ""
		},
		{
			"key": "ciudad",
			"value": ""
		}
	]
}
END

mkdir -p features

cat > features/environment.py<<END
import allure
from allure_commons.types import AttachmentType

def before_scenario(context, scenario):
    context.allure = allure

def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.response.text, name="Response Body", attachment_type=AttachmentType.TEXT)

END

cat > features/my_test.feature<<END
Feature: Test API con Postman

  Scenario: Realizar una solicitud GET a la API
    Given que tengo la URL de la API
    When envío una solicitud GET
    Then se debe recibir una respuesta exitosa

END

mkdir -p features/steps

cat > features/steps/test_steps.py<<END
from behave import given, when, then
from utils import postman_utils as PU


@given('que tengo la URL de la API')
def step_given_setup_endpoint(context):
    pass

@when('envío una solicitud GET')
def step_when_send_request(context):
    PU.ejecutar_postman('colection/postman_collection.json', 'allure')

@then('se debe recibir una respuesta exitosa')
def step_then_verify_status_code(context):
    pass
    

# cambiar ruta*
# script instalación
# assertion
# test postman*
END

mkdir -p utils

cat > utils/postman_utils.py<<END
import os

def ejecutar_postman(path_postman_collection, formato='json'):
    current_path = os.getcwd()
    comando = f'newman run {current_path}/{path_postman_collection}'
    comando += f' -r {formato}'
    os.system(comando)

END

mkdir -p utils/__pycache__

base64_file="yw0NCgAAAABxpsdm7AAAAOMAAAAAAAAAAAAAAAACAAAAAAAAAPMUAAAAlwBkAGQBbABaAGQDZAKEAVoBeQEpBOkAAAAATmMCAAAAAAAAAAAAAAAEAAAAAwAAAPN2AAAAlwB0AQAAAAAAAAAAagIAAAAAAAAAAAAAAAAAAAAAAACrAAAAAAAAAH0CZAF8ApsAZAJ8AJsAnQR9A3wDZAN8AZsAnQJ6DQAAfQN0AQAAAAAAAAAAagQAAAAAAAAAAAAAAAAAAAAAAAB8A6sBAAAAAAAAAQB5ACkETnoLbmV3bWFuIHJ1biD6AS96BCAtciApA9oCb3PaBmdldGN3ZNoGc3lzdGVtKQTaF3BhdGhfcG9zdG1hbl9jb2xsZWN0aW9u2gdmb3JtYXRv2gxjdXJyZW50X3BhdGjaB2NvbWFuZG9zBAAAACAgICD6T0M6XFVzZXJzXEhQXERlc2t0b3BcU2hhcmVkRm9sZGVyXFRlc0FwaVx0ZXN0X2FwaV9wb3N0bWFuXHV0aWxzXHBvc3RtYW5fdXRpbHMucHnaEGVqZWN1dGFyX3Bvc3RtYW5yDQAAAAMAAABzPgAAAIAA3BMVlzmROZM7gEzYEBuYTJg+qBHQK0LQKkPQDkSAR9gEC5AUkGeQWdAPH9EEH4BH3AQGh0mBSYhn1QQW8wAAAAApAdoEanNvbikCcgUAAAByDQAAAKkAcg4AAAByDAAAAPoIPG1vZHVsZT5yEQAAAAEAAABzDQAAAPADAQEB2wAJ9AQEARdyDgAAAA=="
echo "$base64_file" | base64 -d > utils/__pycache__/postman_utils.cpython-312.pyc


###############################################################################
###############################################################################

cd ..
cd ..