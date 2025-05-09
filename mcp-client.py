import asyncio
import logging
from dolphin_mcp import run_interaction

logger = logging.getLogger("dolphin_mcp")
logger.setLevel(logging.INFO)

user_query = """
You are given a running microservices-based system. Your task is to use existing fault injection functions to perform controlled fault injections on the system.

You can also use existing functions to obtain the logs of a service and the results of load tests. Attention: the results of the load tests are aggregated from the beginning of the system operation.

You may want to delete unnecessary experiments to avoid affecting the results of new experiments.

After performing fault injections, you need to observe system behavior and determine whether the following fault tolerance mechanisms are implemented:

- Timeout control
- Retry mechanism
- Circuit Breaker
- Service degradation (fallbacks)
- Rate limiting
- Replicate (multiple instances)

For each mechanism:

Identify if it is present or absent.

Provide evidence or reasoning based on the system's response during fault injection (e.g., timeouts, retries, error messages, fallback behavior).

Attention: All fault tolerance mechanisms are implemented at the the system level, not at the service level. 

Present your finding as a structured report.
"""


async def main():
    result = await run_interaction(
        user_query=user_query,
        model_name="qwen-max",
        config_path="mcp_config.json",
        quiet_mode=False,
        log_messages_path="log.json",
    )
    print(result)

# Run the async function
asyncio.run(main())
