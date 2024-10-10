from agent import createAgent
from livekit.agents import JobContext, WorkerOptions, cli

async def entrypoint (ctx: JobContext):
  await createAgent(ctx)

if __name__ == "__main__":
  cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))