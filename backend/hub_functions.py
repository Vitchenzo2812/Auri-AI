import os
import aiohttp
import logging
import openai

from dotenv import load_dotenv
from typing import Annotated
from livekit.agents import llm
from urllib.parse import quote

load_dotenv()
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

logger = logging.getLogger("hub ai functions")
logger.setLevel(logging.INFO)

image_links = {
  "piso um": "https://auri-maps.s3.us-east-1.amazonaws.com/shopping-porto-piso1.jpg",
  "piso dois": "https://auri-maps.s3.us-east-1.amazonaws.com/shopping-porto-piso2.jpg",
  "piso três": "https://auri-maps.s3.us-east-1.amazonaws.com/shopping-porto-piso3.jpg"
}

class AgentInstructions (llm.FunctionContext):
  def __init__(self) -> None:
    super().__init__()
  
  @llm.ai_callable(description="Get weather of a specific location")
  async def get_weather(self, location: Annotated[
    str, 
    llm.TypeInfo(description="The specific location")
  ]):
    logger.info(f"get weather - location {location}")  

    encoded_location = quote(location)
    url = f"http://api.weatherstack.com/current?access_key={WEATHERSTACK_API_KEY}&query={encoded_location}"
    
    async with aiohttp.ClientSession() as session:
      try:
        async with session.get(url) as response:
          if (response.status != 200):
            return f"Não consegui pegar o clima de {location}"
          
          weather_data = await response.json()
          temperature = weather_data["current"]["temperature"]
          return f"O clima em {location} é {temperature}Cº"
      except Exception as e:
        logger.error(f"Ocorreu esse erro: {e}")

  @llm.ai_callable(description="Describe an image based on a keyword")
  async def describe_image(self, keyword: Annotated[
    str,
    llm.TypeInfo(description="Keyword to describe the image")
  ]):
    logger.info(f"Describing image for keyword: {keyword}")

    image_url = image_links.get(keyword, None)

    if not image_url:
      return f"Não encontrei uma imagem referente a palavra {keyword}"

    try:
      response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
          {
            "role": "user",
            "content": [
              { 
                "type": "image_url",
                "image_url": {
                  "url": image_url
                }
              }
            ]
          }
        ]
      )

      description = response.choices[0].message.content
      return description
    except Exception as e:
      logger.error(f"Ocorreu esse erro: {e}")
