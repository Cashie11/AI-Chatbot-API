# AI Chatbot API

A Django-based REST API that integrates with OpenAI's GPT models to provide conversational AI responses.

## Features

- JSON-based API endpoint
- OpenAI GPT-3.5 Turbo integration
- Error handling and validation
- Configurable response parameters

## Prerequisites

- Python 3.8+
- Django 4.0+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Cashie11/AI-Chatbot-API.git
cd chatbot-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

Send POST requests to `/chatbot/` with JSON payload:

```json
{
    "message": "Your question here"
}
```

Example response:
```json
{
    "message": "AI response here",
    "success": true
}
```

## API Reference

### POST /chatbot/

Parameters:
- `message` (string, required): User input message

Response:
- `message` (string): AI-generated response
- `success` (boolean): Operation status
- `error` (string, optional): Error message if applicable

## Development

1. Start local server:
```bash
python manage.py runserver
```

2. Access API at `http://localhost:8000/chatbot/`

## Error Handling

- 400: Invalid JSON or missing message
- 405: Method not allowed
- 500: Server/API errors

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License - Feel free to use and modify

## Contact

Name - frankizuchukwu094@gmail.com
Project Link: https://github.com/Cashie11/AI-Chatbot-API.git
