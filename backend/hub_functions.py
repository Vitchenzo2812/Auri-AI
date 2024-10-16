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

  @llm.ai_callable(description="Describe an image")
  async def describe_image(self, image_url: Annotated[
    str,
    llm.TypeInfo(description="URL of image")
  ]):
    logger.info(f"Describing the image... {image_url}")

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
                  "url": "https://images.unsplash.com/photo-1494145904049-0dca59b4bbad?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
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
