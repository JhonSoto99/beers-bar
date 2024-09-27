# Beers Bar Backend y Frontend

Este proyecto contiene un backend desarrollado en FastAPI para manejar la lógica de pedidos y stock.
Y un Frotend desarrollado en Next.js para visualizar los datos.

## Requisitos

- Python 3.12
- Next.js 14.2.13
- React.js 18
- Node 21.6.1

## Instalación Bakend

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
   - [http://0.0.0.0:5000/api/docs](http://0.0.0.0:5000/api/docs)
   - [http://0.0.0.0:5000/api/redoc](http://0.0.0.0:5000/api/redoc)


## Documentación de la API:
   A la documentación de la API se puede acceder en:

   - Swagger:
     [http://0.0.0.0:5000/api/docs](http://0.0.0.0:5000/api/docs)
   
   - Redoc
     [http://0.0.0.0:5000/api/redoc](http://0.0.0.0:5000/api/redoc)

## Pruebas

Este proyecto incluye pruebas automatizadas para garantizar la funcionalidad y la calidad del código. A continuación, se indican los pasos para ejecutar las pruebas.

Para ejecutar las pruebas, utiliza el siguiente comando:
```bash
  cd backend/
  pytest
```

## Instalación Frontend

3. **Instala las dependencias:**
   ```bash
   npm install

4. **Configurar archivo .env:**

    Se debe configurar el host del backend en un archivo .env en la raiz del proyecto fronted,
    en el respositorio hay una plantilla llamada env.example para crear el archivo .env

    debería quedar asó:
    ```bash
       .env
       API_URL="http://0.0.0.0:5000"
    ```

4. **Ejecución del Proyecto:**
   ```bash
   npm run dev
   ```

## Pruebas

Este proyecto incluye pruebas automatizadas para garantizar la funcionalidad y la calidad del código. A continuación, se indican los pasos para ejecutar las pruebas.

Para ejecutar las pruebas, utiliza el siguiente comando:
```bash
  cd frontend/
  npm run test
```