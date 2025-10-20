from openai import OpenAI
from app.config import Config
import json

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def identify_marble_style(image_data):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": '''Analyze this glass marble image and identify its style. 
                            Common styles include: Latticino, Lutz, Swirl, Onionskin, Mica, 
                            End of Day, Cat's Eye, Clambroth, Sulphide, Contemporary Art.
                            Respond with JSON: {"style": "style_name", "confidence": 0-100, 
                            "description": "brief description"}'''
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        return {"error": str(e)}
