import asyncio
import json
from web3 import Web3

import discord
from discord.ext import commands


CHANNEL_ID = 937226359623798858

DISCORD_BOT_TOKEN = "OTM3MjI2MDQ5MjM2OTI2NDc1.GzEuhf.bz3ctE4kwSXT5rNQMWR6RvM2WF7p4aUNjyKALE" #"ODk3NTU4NzQ3NTU4MzE0MDQ0.YWXauQ.XAstCrblSXDAvq2xmZWcHLvprr4" #os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="nftg-", intents=intents)

CONTRACT_ADDRESS = "0x54B9CCfEB393712d13f13c6944b81ce983e2D62a"


with open("contracts/ABI.json") as f:
    ABI = json.load(f)


async def log_loop(event_filter):
    while True:
        for APICallMade in event_filter.get_new_entries():
            event_json = Web3.toJSON(APICallMade)
            channel = bot.get_channel(int(CHANNEL_ID))
            
            event_json = json.loads(event_json)
            event_json_args = event_json["args"]
            #print(event_json_args)
            wallet = event_json_args["caller"]
            query_id = event_json_args["queryId"]


            #token_id = (str(event_json).split(",")[1]).split(": ")[-1].replace("}", "").replace(" ", "") #(str(event_json).split(",")[0]).split(": ")[-1][0:-1]
            embed_channel = discord.Embed(title="Dune API Query Made For Query ID : " + str(query_id) + " By " + wallet[0:5] + "...." + wallet[-4::], color=0xe67e22, url = "https://polygonscan.com/tx/" + event_json["transactionHash"])
            embed_channel.set_image(url="https://gateway.pinata.cloud/ipfs/QmYCov5mrqcNxGdH43ifD8HPtyQ3TzY8MhEknzgXwfwRde")
            await channel.send(embed=embed_channel)
            
            #await asyncio.sleep(3)
            #print(event_json["args"]["totalMinted"])
            
        await asyncio.sleep(1)

def track_mint_event():
    polygon = "wss://polygon-mainnet.g.alchemy.com/v2/LnkyQ4zs7KRB_H6xDdG0vd86QnLXX_KO"
    #print(ABI)
    #polygon = "https://rpc.ankr.com/polygon"
    web3 = Web3(Web3.WebsocketProvider(polygon))
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
    #print(contract.events.TokenMinted)
    event_filter = contract.events.APICallMade.createFilter(fromBlock='latest')
    #block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter)))
                # log_loop(block_filter, 2),
                # log_loop(tx_filter, 2)))
    finally:
        # close loop to free up system resources
        loop.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(DISCORD_BOT_TOKEN))
    loop.create_task(track_mint_event())
    loop.run_forever()