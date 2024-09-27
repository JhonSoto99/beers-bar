# Beers Bar Backend

Este proyecto es un backend desarrollado en FastAPI para manejar la lógica de pedidos y stock.

## Requisitos

- Python 3.12

## Instalación con Docker

1. **Clona el repositorio:**

   ```bash
   git clone git@github.com:JhonSoto99/beers-bar.git
   cd beers-bar

2. **Construye el contenedor docker:**

   ```bash
   docker-compose build

2. **Levanta el contenedor docker:**

   ```bash
   docker-compose up -d
   ```
   Esto iniciará el servidor.
   La aplicación estará disponible en:
   - [http://localhost:8080/api/docs](http://localhost:8080/api/docs)
   - [http://localhost:8080/api/redoc](http://localhost:8080/api/redoc)



## Instalación sin Docker

1. **Clona el repositorio:**

   ```bash
   git clone git@github.com:JhonSoto99/beers-bar.git
   cd beers-bar/backend

2. **Crea un entorno virtual (opcional, pero recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   
4. **Ejecución del Proyecto:**
   ```bash
   uvicorn app.main:app --reload --port 5000 --host 0.0.0.0
   ```
   
   Esto iniciará el servidor en modo de recarga automática.
   La aplicación estará disponible en:
   - [http://127.0.0.1:5000/api/docs](http://localhost:8080/api/docs)
   - [http://127.0.0.1:5000/api/redoc](http://localhost:8080/api/redoc)


## Documentación de la API:
   A la documentación de la API se puede acceder en:

   - Swagger:
   http://127.0.0.1:5000/api/docs
   
   - Redoc
   http://127.0.0.1:5000/api/redoc

## Pruebas

Este proyecto incluye pruebas automatizadas para garantizar la funcionalidad y la calidad del código. A continuación, se indican los pasos para ejecutar las pruebas.

Para ejecutar las pruebas, utiliza el siguiente comando:
```bash
  cd backend/
  
  export PYTHONPATH=$(pwd) # Linux
  set PYTHONPATH=%cd% # windows

  pytest
```