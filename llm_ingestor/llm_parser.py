import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

def parse_prompt(prompt_text: str) -> dict:
    # Use OpenAI to extract structured metadata
    # You may use a prompt template that instructs the LLM to output JSON
    completion = openai.ChatCompletion.create(
        model="gpt-4",  # or gpt-3.5 etc
        messages=[
            {
                "role": "system",
                "content": "You extract metadata for a data ingestion pipeline. Output valid JSON."
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        temperature=0.0
    )
    resp = completion.choices[0].message.content.strip()
    import json
    metadata = json.loads(resp)
    return metadata

