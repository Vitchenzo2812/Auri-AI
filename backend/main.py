from agent import createAgent
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.plugins import silero

async def entrypoint (ctx: JobContext):
  await createAgent(ctx)

if __name__ == "__main__":
  cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))