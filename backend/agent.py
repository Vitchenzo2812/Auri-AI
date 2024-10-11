import os
import asyncio

from dotenv import load_dotenv
from hub_functions import AssistantFnc
from livekit.agents import AutoSubscribe, JobContext, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, cartesia, silero, deepgram

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

  fnc_ctx = AssistantFnc()

  assistant = VoiceAssistant(
      vad=silero.VAD.load(),
      stt=deepgram.STT(language="pt-BR"),
      llm=openai.LLM(),
      tts=cartesia.TTS(
        model="sonic-multilingual",
        language="pt",
        voice=CARTESIA_VOICE_ID
      ),
      chat_ctx=initial_ctx,
      fnc_ctx=fnc_ctx
  )

  assistant.start(ctx.room)

  await asyncio.sleep(1)
  await assistant.say(f"Olá, como posso te ajudar hoje?", allow_interruptions=True)