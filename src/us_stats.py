import asyncio
import json
import aiohttp
from understat import Understat


async def main():
    async with aiohttp.ClientSession() as session: # TODO check what async does
        understat = Understat(session)
        team_stats = await understat.get_team_stats("Chelsea", 2020)
        formation_list = list(team_stats["formation"].keys())
        for formation in team_stats["formation"]:
            xg = team_stats["formation"][formation]["xG"]
            xg_against = team_stats["formation"][formation]["against"]["xG"]
            minutes = team_stats["formation"][formation]["time"]
            print(f"{formation}: xG: {xg}, xGA: {xg_against} in {minutes} mins")

        # print(json.dumps(team_stats["formation"], indent=4, sort_keys=True))
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())