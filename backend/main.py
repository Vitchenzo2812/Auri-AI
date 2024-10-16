from agent import create_agent
from livekit.agents import JobContext, JobProcess, WorkerOptions, cli
from livekit.plugins import silero

def prewarm (proc: JobProcess):
  proc.userdata["vad"] = silero.VAD.load()

async def entrypoint (ctx: JobContext):
  await create_agent(ctx)

if __name__ == "__main__":
  cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))