import os
import logging
import asyncio

from dotenv import load_dotenv
from hub_functions import AgentInstructions
from livekit.agents import AutoSubscribe, JobContext, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, cartesia, deepgram

logger = logging.getLogger("create agent")
logger.setLevel(logging.INFO)

load_dotenv()
CARTESIA_VOICE_ID = os.getenv("CARTESIA_VOICE_ID")

async def create_agent (ctx: JobContext):  
  initial_ctx = llm.ChatContext().append(
    role="system",
    text=(
        "Você é um assistente de voz, seu nome é Auri. Sua interface com os usuários será por voz."
        "Você deve usar respostas curtas e concisas, evitando o uso de pontuações impronunciáveis."
        "Você é um assistente voltado a acessibilidade para pessoas cegas e surdas."
      )
  )

  await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

  agent_instructions_ctx = AgentInstructions()

  vad = (ctx.proc.userdata["vad"])

  agent = VoiceAssistant(
      vad=vad,
      stt=deepgram.STT(language="pt-BR"),
      llm=openai.LLM(),
      tts=cartesia.TTS(
        model="sonic-multilingual",
        language="pt",
        voice=CARTESIA_VOICE_ID
      ),
      chat_ctx=initial_ctx,
      fnc_ctx=agent_instructions_ctx
  )

  participant = await ctx.wait_for_participant()
  agent.start(ctx.room, participant)

  await asyncio.sleep(1)
  await agent.say("Olá, como posso ajudar?")