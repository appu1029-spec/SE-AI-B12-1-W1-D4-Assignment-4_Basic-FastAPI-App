from fastapi import FastAPI

# Create the FastAPI application.
app = FastAPI(
    title="Arokia's Basic FastAPI App",
    description="My first API with a welcome endpoint and a greeting endpoint.",
    version="1.0.0",
)


# Root endpoint: http://127.0.0.1:8000/
@app.get("/")
def welcome():
    """Return a simple welcome message."""
    return {"message": "Hello, FastAPI"}


# Path parameter endpoint: http://127.0.0.1:8000/greet/Arokia
@app.get("/greet/{name}")
def greet(name: str):
    """Return a greeting using the name supplied in the URL."""
    return {
        "message": f"Hello, {name}! Welcome to my FastAPI app.",
        "name": name,
    }