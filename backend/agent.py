import os
import asyncio

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero, cartesia

load_dotenv()
CARTESIA_VOICE_ID = os.getenv("CARTESIA_VOICE_ID")
CARTESIA_LANGUAGE = os.getenv("CARTESIA_LANGUAGE")

async def createAgent (ctx: JobContext):
  initial_ctx = llm.ChatContext().append(
    role="system",
    text=(
        "Você é um assistente de voz, seu nome é Auri. Sua interface com os usuários será por voz."
        "Você deve usar respostas curtas e concisas, evitando o uso de pontuações impronunciáveis."
        "Você é um assistente voltado a acessibilidade para pessoas cegas."
      )
  )

  await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

  assistant = VoiceAssistant(
      vad=silero.VAD.load(min_silence_duration=1),
      stt=openai.STT(language="pt"),
      llm=openai.LLM(),
      tts=cartesia.TTS(
        model="sonic-multilingual",
        language=CARTESIA_LANGUAGE,
        voice=CARTESIA_VOICE_ID
      ),
      chat_ctx=initial_ctx
  )

  assistant.start(ctx.room)

  await asyncio.sleep(1)
  await assistant.say("Olá, como posso te ajudar hoje?", allow_interruptions=True)