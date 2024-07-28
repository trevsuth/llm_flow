# Narvaez
A locally run LLM implementation

## Instructions
1. Build docker container `docker build -t narvaez`
1. Run docker container `docker run -d -p 80:80 narvaez`

## Use:
`curl -X POST "http://localhost/invoke" -H "Content-Type: application/json" -d '{"input": "Tell me a joke"}'`