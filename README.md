# LangServe with Gemini & Groq

A small project that exposes two LLMs (**Google Gemini** and **Groq**) as REST API endpoints using **FastAPI** and **LangServe**, along with a simple Python client that calls them.

## How it works

```
client.py  ──HTTP POST──▶  FastAPI + LangServe (main.py)  ──▶  Gemini / Groq
 (question)                  /gemini/tech, /groq/nontech         (answer)
```

1. `main.py` builds two LangChain chains (`prompt | model`) and registers each one as an API route with LangServe.
2. `client.py` sends a question to those routes and prints the model's reply.

## Tech stack

- Python 3.12+
- FastAPI
- LangChain
- LangServe
- langchain-google-genai (Gemini)
- langchain-groq (Groq)
- Uvicorn
- python-dotenv, requests

## Project structure

```
langserve-gemini-groq/
├── main.py            # FastAPI + LangServe server
├── client.py          # Client that calls the API endpoints
├── requirements.txt   # Dependencies
├── .env               # API keys (NOT committed to git)
├── .gitignore
└── README.md
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/langserve-gemini-groq.git
cd langserve-gemini-groq
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

- Windows: `venv\Scripts\activate`
- macOS / Linux: `source venv/bin/activate`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API keys

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Get your keys here:

- Gemini: [Google AI Studio](https://aistudio.google.com/)
- Groq: [Groq Console](https://console.groq.com/)

> **Never commit your `.env` file.** Make sure `.env` is listed in `.gitignore`.

## Running the project

You need **two terminals**.

**Terminal 1: start the server**

```bash
uvicorn main:app --reload
```

Wait until you see `Application startup complete.` and leave this terminal running.

**Terminal 2: run the client**

```bash
python client.py
```

## API endpoints

| Endpoint | Model | Description |
| --- | --- | --- |
| `POST /gemini/tech/invoke` | Gemini | Ask Gemini a question |
| `POST /groq/nontech/invoke` | Groq | Ask Groq a question |

LangServe also generates `/stream`, `/batch` and `/playground` for each route.

Useful URLs once the server is running:

- Swagger docs: http://localhost:8000/docs
- Gemini playground: http://localhost:8000/gemini/tech/playground/
- Groq playground: http://localhost:8000/groq/nontech/playground/

### Example request

```bash
curl -X POST http://localhost:8000/gemini/tech/invoke \
  -H "Content-Type: application/json" \
  -d '{"input": {"topic": "What is Python?"}}'
```

The model's reply is in `output.content` of the JSON response.

## Troubleshooting

**`WinError 10061: target machine actively refused it`**
The server is not running. Start it in a separate terminal with `uvicorn main:app --reload` before running `client.py`.

**`ModuleNotFoundError`**
Dependencies are missing. Activate your virtual environment and run `pip install -r requirements.txt`.

**Authentication / API key errors**
Check that `.env` exists and the variable names are exactly `GOOGLE_API_KEY` and `GROQ_API_KEY`.

## Ideas for improvement

- Use different prompts for the tech and non-tech routes
- Add a single endpoint that decides which model to use based on the question
- Add streaming responses in the client
- Dockerize the app

## License

This project is open source. Add a license of your choice (for example MIT).
