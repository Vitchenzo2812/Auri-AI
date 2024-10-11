import os
import aiohttp
import logging

from dotenv import load_dotenv
from typing import Annotated
from livekit.agents import llm
from urllib.parse import quote

load_dotenv()
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")

logger = logging.getLogger("hub ai functions")
logger.setLevel(logging.INFO)

class AssistantFnc (llm.FunctionContext):
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
          logger.info(weather_data)
          temperature = weather_data["current"]["temperature"]
          logger.info(temperature)
          return f"O clima em {location} é {temperature}Cº"
      except Exception as e:
        logger.error(f"Ocorreu esse erro: {e}")