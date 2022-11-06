# Duned Powered By Dune, Polygon, Uniswap & IPFS

----------------

## Duned In A Nutshell

A token-gated data extraction platform whose metadata is stored on IPFS (Pinata) and built on Polygon to utilise Dune's API to download data on a pay per call basis using a non-transferrable subscriber NFT.

----------------

## Some Important Links
- Non Transferrable NFT Contract On Polygon - https://polygonscan.com/address/0x86503B0FFbEbd75970d710cb3117e6d7571041A8
- API Tracker Contract On Polygon - https://polygonscan.com/address/0x54B9CCfEB393712d13f13c6944b81ce983e2D62a 
- NFT Image On Pinata - https://gateway.pinata.cloud/ipfs/QmYCov5mrqcNxGdH43ifD8HPtyQ3TzY8MhEknzgXwfwRde
- NFT Metadata On Pinata - https://gateway.pinata.cloud/ipfs/QmSpJgyaqExFYsyKPvkDnugUsijCKA3WRKEiwsAoG1gtVN

----------------

## Duned - In Depth

To make use of APIs, we usually use a certain API key and make a request to a URL. However, this has a lot of drawbacks:
  - Not everyone knows how to utlise APIs
  - API Keys can be transferred, thereby resulting in loss of revenue for companies
  - People could use APIs to bypass and procure certain features only available in Pro subscription plans
  - People might not always want to purchase a Pro subscription as they might have a very limited use-case for which a subscription plan could be an overkill.
  
In order to address these issues, I built a simple and cool app. <br>
The idea of the app is to use NFTs as a way to grant entrance to using the Dune API. Since Dune's API can allow people to get data off their platform and into their local machines, there needs to be an incentive for Dune as a paltform.<br>

For anyone who wants to use the Dune API to download data in their local machines, they will first have to mint a `Dune SubNFT on Polygon` by paying a certain amount (for the purpose of this hackathon that amount is 0.1 $MATIC). The metadata and image associated with this NFT has been uploaded to IPFS using Pinata. Once someone has the Dune SubNFT, they can now download data from any existing query on Dune!! But there's a catch!

Since data is getting off Dune' platform, there needs to be an incentive and the incentive here is that, for every download call you make using this platform, a certain amount goes to Dune. All these transactions will again be on Polygon and all you'll have to do is pay per call for downloading the data (for the purpose of this hackathon the cost per call is 0.1 $MATIC). Once the payment is successful, the user will be expected to submit the query number and the data associated with that query will automatically be downloaded onto your local system.

Finally, since we interact with smart contracts to track payments and then allow users to download data, the best part is that all this data is on chain and every time a query is made, events are emitted from the contract which are streamed into discord channels. 

Also, the project solves a problem statement that uniswap foundation mentioned. Data collection can prove to be extremely tedious but through this platform and Dune's API, the latest 100,000 transactions' data can be procured at the click of a button in a matter of seconds.

PS : Since data is on-chain, this in itself could be a super cool Dune Dashboard - A Dashboard to track API Usage!!!!

PPS : I made a super sleek PyDune module ;) People would be able to download this with pip and insert their API key and get query results in one line of code!

------------
## So What Does This Solve?
  - Acts as a super cool tool for those who don't know how to code but want to download some data and import it into Excel
  - Super convenient tool for DAOs - they can get a plethora of data for low rates and perform analysis - solves them the issue to capture and store data!
  - Since the NFT is non-transferrable, every wallet needs to have a new NFT. This removes the issue of sharing of API keys!!
  - Although data is coming off the platform and is kind of like a pro feature being utilised, the incentive is that Dune still gets paid for getting data off their platforms.
  - It's a win-win for Dune and users because users can now download data without getting the Pro plan and Dune still gets paid if someone is downloading data without being on the Pro plan.
  - Adds additional security to APIs ;)
  - And <b> IT'S SUPER COOL!!!!</b>
  
-------------
## Nitty Gritties Of The Project

The project was mainly built using the following languages:
- Dune
- Uniswap
- Polygon
- IPFS
- Python
- Flask
- HTML
- CSS
- JavaScript
- Solidity
- Heroku
- Discord

Python and Flask essentially form the backend. This is how all Dune queries are processed and the data download is facilitated. However, this cannot be done all alone. We need query ids from users which is gotten from the frontend. The frontend was built using HTML, CSS & JavaScript. JavaScript handles all web3 functions, like allowing users to mint NFTs if they don't have one already, checking for NFTs and providing token gated access to platform, allowing users to pay per download, etc. All web3 functions are being handled by JavaScript. Solidity is used for writing the NFT contract & the API Tracker contract that handled the pay per download aspect. These smart contracts are deployed on Polygon. And oh, Polygon was super fast and super cheap! Like wow! Transactions happen in that very instant almost. The image and metadata associated with the NFTs are uploaded to Pinata. And like always, Pinata was a saviour. It's amazing how easy it is to upload data and create baseURIs for NFT contracts using IPFS technology and Pinata's service. Go IPFS!!!!! Every time an API call is made using this platform, it emits an event from the contract which is captured and streamed directly into a discord channel. The platform itself is deployed on Heroku. Finally this entire project would not be possible without Dune and their API!

Also, in the end I utilised Dune's API and my product to be able to facilitate extremely quick download of Uniswap data for the latest 100,000 transactions at the click of a button!

I was particularly impressed by how I was able to build an end-to-end pipeline while working all alone. I did not have the inspiration to build something cool until 2pm on 5th November. But talking to Dune and playing with their API just gave me some inspiration to think of something that could be useful. I did something hacky initially and that was to simply facilitate download of data using the API but this by-passed the Dune Pro Plans. That's when I thought why not solve this security problem itself and then facilitate the download of data using the API. Being able to do all of this alone in a span of hardly 10 hours really gave me a lot of confidence in my abilities as a developer!
  
