# Brain Tumor Detection
Front-end for medical image classifier Machine Learning model (CNN)

## Run the Flask app

To run your Flask app, execute the following command in your terminal:

```bash
python app.py
```

By default, Flask will start a development server on `http://127.0.0.1:5000/`. You can access your app by navigating to this URL in your web browser.

## Use a production WSGI HTTP server

For production environments, it's recommended to use a WSGI HTTP server like Gunicorn or uWSGI, which will handle requests more efficiently than the development server. To run your Flask app with Gunicorn, use:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```
