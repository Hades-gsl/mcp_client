import asyncio
import logging
from time import sleep
from dolphin_mcp import run_interaction, SSEMCPClient

# logger = logging.getLogger("dolphin_mcp")
# logger.setLevel(logging.INFO)


async def main():
    result = await run_interaction(
        user_query="Hello, give me the results of the load test",
        model_name="qwen-max",  # Optional, will use default from config if not specified
        config_path="mcp_config.json",  # Optional, defaults to mcp_config.json
        quiet_mode=False,  # Optional, defaults to False
        log_messages_path="log.json",
    )
    print(result)

# Run the async function
asyncio.run(main())
