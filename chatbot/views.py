import json
from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Initialize OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        try:
            # Parse JSON payload
            data = json.loads(request.body)
            user_input = data.get('message', '').strip()

            # Validate input
            if not user_input:
                return JsonResponse({
                    'error': 'No message provided',
                    'success': False
                }, status=400)

            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=100,
                temperature=0.7,
            )

            # Extract AI response
            ai_response = response.choices[0].message.content.strip()

            # Return JSON response
            return JsonResponse({
                'message': ai_response,
                'success': True
            })

        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON',
                'success': False
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': str(e),
                'success': False
            }, status=500)

    # Handle non-POST requests
    return JsonResponse({
        'error': 'Only POST requests are allowed',
        'success': False
    }, status=405)