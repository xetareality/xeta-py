# Official Python Client for Xeta

Official Python client to interact with Xeta Blockchain and Xeta Blockchain Interface.

Xeta is a serverless layer-1 blockchain for Metaverse, Gaming, and NFT applications that provides infinite scalability, high throughput, sub-second confirmation times, and fees at a tenth of a cent. Xeta achieves this by leveraging serverless compute and storage cloud services while innovating incentive structures and extending the Byzantine Fault Tolerance consensus mechanism for scalability.

# General

Install Xeta through pip, import it, generate a public/private key (or use your existing ones) and start building using the examples below.

```
# Installation
pip install xeta

# Imports
import xeta

# Generate and connect a keypair
public, private = xeta.crypto.generate_keypair()
xeta.connect(public, private)
```

# Interface

The interface methods allow to interact with storage nodes for read-only functionality. Using these methods, you could build a similar frontend app like our [**network explorer**](https://xeta.network). Interface requests are free, but rate-limited and should allow for "regular" usage. Please contact us at developers@xetareality.com if you would like to have dedicated limits.

## Transaction

```
# Get a transaction by signature
xeta.transaction.get(signature=SIGNATURE)

# Batch get transactions by signatures
xeta.transaction.batchGet(signatures=[SIGNATURE, SIGNATURE])

# Poll a transaction by signature
xeta.transaction.poll(signature=SIGNATURE, interval=0.5, timeout=5)

# Scan transactions by from-address
xeta.transaction.scanByFrom(from_address=ADDRESS, sort='DESC', limit=25)

# Scan transactions by to-address
xeta.transaction.scanByTo(to=ADDRESS, sort='DESC', limit=25)

# Scan transactions by sender-address
xeta.transaction.scanBySender(sender=ADDRESS, sort='DESC', limit=25)

# Scan transactions by token
xeta.transaction.scanByToken(token=ADDRESS, sort='DESC', limit=25)

# Scan transactions by period
xeta.transaction.scanByPeriod(period=YYMMDDHH, sort='DESC', limit=25)

# Scan transactions by from and token
xeta.transaction.scanByFromToken(from_address=ADDRESS, token=ADDRESS, sort='DESC', limit=25)

# Scan transactions by to and token
xeta.transaction.scanByToToken(to=ADDRESS, token=ADDRESS, sort='DESC', limit=25)
```

## Token

```
# Get a token by address
xeta.token.get(address=ADDRESS)

# Batch get tokens by addresses
xeta.token.batchGet(signatures=[SIGNATURE, SIGNATURE])

# Scan tokens by creator
xeta.token.scanByCreator(creator=ADDRESS, sort='DESC', limit=25)

# Scan tokens by ticker
xeta.token.scanByTicker(ticker='XETA', sort='DESC', limit=25)

# Scan tokens by name
xeta.token.scanByName(name'Xeta', sort='DESC', limit=25)
```

## Pool

```
# Get a pool by address
xeta.pool.get(address=ADDRESS)

# Scan pools by creator
xeta.pool.scanByCreator(creator=ADDRESS, sort='DESC', limit=25)

# Scan pools by token
xeta.pool.scanByToken(token=ADDRESS, sort='DESC', limit=25)

# Scan pools by name
xeta.pool.scanByName(name'Xeta Staking', sort='DESC', limit=25)
```

## Allowance

```
# Get an allowance for address, token and spender
xeta.allowance.get(address=ADDRESS, token=ADDRESS, spender=ADDRESS)

# Get an allowance by hash
xeta.allowance.getByHash(hash=HASH)

# Scan allowances by address
xeta.allowance.scanByAddress(address=ADDRESS, sort='DESC', limit=25)

# Scan allowances by spender
xeta.allowance.scanBySpender(spender=ADDRESS, sort='DESC', limit=25)
```

## Audit

```
# Get audit of a token-balance
xeta.audit.balance(address=ADDRESS, token=ADDRESS, limit=5)

# Get audit of a xeta-balance
xeta.audit.xeta(address=ADDRESS, limit=5)

# Get audit of a transaction
xeta.audit.transaction(signature=SIGNATURE)

```

## Balance

```
# Get a balance by address and token
xeta.balance.get(address=ADDRESS, token=ADDRESS)

# Scan balances by address
xeta.balance.scanByAddress(address=ADDRESS, sort='DESC', limit=25)

# Scan balances by token
xeta.balance.scanByToken(token=ADDRESS, sort='DESC', limit=25)
```

## Candle

```
# Scan candles by token and interval (currently available: 5m, 1h, 4h, 1d, 1w)
xeta.candle.scan(token=ADDRESS, interval=INTERVAL, sort='DESC', limit=100)
```

## Claim

```
# Get a claim by address, token and owner
xeta.claim.get(address=ADDRESS, token=ADDRESS, owner=ADDRESS)

# Get a claim by hash
xeta.claim.getByHash(hash=HASH, sort='DESC', limit=25)

# Scan claims by amount
xeta.claim.scanByAmount(owner=ADDRESS, sort='DESC', limit=25)

# Scan claims by created
xeta.claim.scanByCreated(owner=ADDRESS, sort='DESC', limit=25)
```

## Stats

Coming soon.

# Modules

Modules are wrapper methods that submit transactions to the network endpoint. Fees for methods are fixed and most recent fees can be found on [docs.xetareality.com](https://docs.xetareality.com). 

## Transaction

```
# Create a basic transaction
xeta.transaction.create({'amount': 10, 'to': ADDRESS, 'token': ADDRESS})

# Create a transaction using an existing allowance
xeta.transaction.create({'amount': 10, 'to': ADDRESS, 'token': ADDRESS, 'from': ADDRESS})

# Create a delegate transaction (fees paid by recipient)
xeta.transaction.create({'amount': 10, 'to': ADDRESS, 'token': ADDRESS, 'delegate'=True})

# Sponsor an address (for XETA fee-delegation)
xeta.transaction.sponsor({'amount': 10, 'to': ADDRESS})

# Batch distribute fungible tokens (up to 10 transfers per request)
xeta.transaction.batch_ft([
    {'to': ADDRESS, 'amount': 5},
    {'to': ADDRESS, 'amount': 5}],
    {'token': ADDRESS, 'amount': 10})

# Batch distribute non-fungible tokens (up to 8 transfers per requests)
xeta.transaction.batch_nft([
    {'to': ADDRESS, 'token': ADDRESS},
    {'to': ADDRESS, 'token': ADDRESS}])
```

## Token

```
# Create a non-fungible token
xeta.token.create({'name': 'Xeta Punk, 'supply': 1, 'object': URL, icon: URL, meta: ATTRIBUTES})

# Create a fungible token
xeta.token.create({'name': 'Bitcoin', 'ticker': 'BTC', 'supply': 21000000, icon: URL})

# Batch create non-fungible tokens (up to 40 tokens per request)
xeta.token.batch([
    {'name': 'Xeta Punk #1', object: URL, icon: URL},
    {'name': 'Xeta Punk #2', object: URL, icon: URL}])

# Mint reserve-supply for a fungible token
xeta.token.mint({'amount': 10}, {'token': ADDRESS})

# Update details for a token (description, links, meta, icon)
xeta.token.update(
    {'description': TEXT, links: [LINK, LINK], meta: TEXT, icon: URL},
    {'token': ADDRESS})
```

## Pool

For pool creation, it is recommended to use the program-specific methods (which are wrappers around this method). Available pool programs are auction, launch, lock, loot, lottery, royalty, stake, swap, vote.

```
# Create a pool
xeta.pool.create({'program': PROGRAM, 'expires': TIMESTAMP}, {'token': ADDRESS})
```

## Allowance

```
# Create an allowance
xeta.allowance.create({'spender': ADDRESS, 'amount': 10}, {'token': ADDRESS})

# Batch create allowances (up to 100 spenders per request)
xeta.allowance.batch([
    {'spender': ADDRESS, 'amount': 10},
    {'spender': ADDRESS, 'amount': 10}],
    {'token': ADDRESS})
```

# Programs

Pools are based on programs, which are pre-written smart contracts on Xeta. For further details on individual functionalities or requirements check out the [Xeta Reality Docs](https://docs.xetareality.com). To get the pool object from pool-address, use the xeta.pool.get interface method.

## Auction

Creator methods:
```
# Create an auction pool
auction = xeta.auction.create(
    {'expires': TIMESTAMP, 'xetaTarget': 10, 'xetaLimit': 100},
    {'token': ADDRESS})

# Deposit the pool-token to be auctioned (FT or NFT)
auction.deposit({'amount': 10})

# Close an auction
auction.close()
```

Participant methods:
```
# Submit a XETA-bid
auction.transfer({'amount': 5})

# Resolve an auction
auction.resolve()

# Cancel an auction
auction.cancel()
```

## Launch

Creator methods:
```
# Create a launch pool
launch = xeta.launch.create(
    {'expires': TIMESTAMP, 'xetaTarget': 10, 'xetaLimit': 100},
    {'token': ADDRESS})

# Deposit the pool-token to be launched
launch.deposit({'amount': 10})

# Withdraw the pool-token
launch.withdraw()

# Close a launch pool
launch.close()
```

Participant methods:
```
# Resolve a launch (if expired or limit is met)
launch.resolve()

# Participate with a XETA transfer
launch.transfer({'amount': 5})

# Swap directly (if launch pool has a swap-rate)
launch.swap({'amount': 5})

# Claim after expiry
launch.claim()
```

## Lock

Creator methods:
```
# Create a lock pool
lock = xeta.lock.create({'expires': TIMESTAMP}, {'token': ADDRESS})
```

Participant methods:
```
# Deposit the pool-token to be locked
lock.transfer({'amount': 10}, unlocks=TIMESTAMP)

# Deposit the pool-token to be locked (unlockable by someone else)
lock.transfer({'amount': 10}, unlocks=TIMESTAMP, address=ADDRESS)

# Claim locked tokens after unlock time expires
lock.claim()
```

## Loot

Creator methods:
```
# Create a loot pool (returns a random NFT with 50% probability, for the participation amount of 5 token)
loot = xeta.loot.create(
    {'probability': 0.5, 'minAmount': 5, 'maxAmount': 5},
    {'token': ADDRESS})

# Deposit an NFT to the loot pool
loot.deposit({'token': ADDRESS})

# Withdraw a deposited NFT
loot.withdraw({'token': ADDRESS})

# Clear a loot pools earnings
loot.clear()
```

Participant methods:
```
# Participate in loot pool
loot.transfer({'amount': 5})
```

## Lottery

Creator methods:
```
# Create a lottery pool
lottery = xeta.lottery.create(
    {'expires': TIMESTAMP, 'claimsLimit': 1000, 'transfersLimit': 10000},
    {'token': ADDRESS})

# Deposit pool tokens to be promoted
lottery.deposit({'amount': 1000})

# Withdraw the deposited pool tokens
lottery.withdraw()

# Close a lottery pool
lottery.close()

# Clear a lottery (if participation is paid)
lottery.clear()
```

Participant methods:
```
# Participate in the lottery
lottery.transfer({'amount': 0})

# Claim after pool expiry/closure
lottery.claim()
```

## Royalty

Creator methods:
```
# Create a royalty pool (30% APY)
royalty = xeta.royalty.create({'rate': 0.3}, {'token': ADDRESS})

# Deposit royalty rewards to the royalty pool
royalty.deposit({'amount': 1000})

# Withdraw deposited royalty rewards
royalty.withdraw()

# Close a royalty pool
royalty.close()
```

Participant methods:
```
# Transfer (make a royalty claim)
royalty.transfer()

# Make a royalty claim
royalty.claim()
```

## Stake

Creator methods:
```
# Create a staking pool (30% APY, 50% bonus, min. 30d lock, max 1y lock, min/max lock amounts)
stake = xeta.stake.create(
    {'rate': 0.3, 'percentage': 0.5, 'minTime': 30*86400000, 'maxTime': 365*86400000, 'maxAmount': 1000000},
    {'token': ADDRESS})

# Deposit stake rewards
stake.deposit({'amount': 1000})

# Withdraw deposited rewards
stake.withdraw()
```

Participate methods:
```
# Create a stake
stake.transfer({'amount': 10}, unlocks=int(time.time()+30*86400000))

# Claim amount and stake rewards
stake.claim()
```

## Swap

Swap pools are automatically created for all fungible tokens, with the same pool-address as the token-address.

Liquidity provider methods:
```
# Deposit the pool-token to be auctioned (FT or NFT)
swap.deposit({'amount': 10, 'token': ADDRESS})

# Supply liquidity (once pool token and XETA has been deposited)
swap.supply()

# Withdraw 50% of supplied liqudity
swap.withdraw(percentage=0.5)
```

Participant methods:
```
# Transfer to swap pool (either pool token or XETA)
swap.transfer({'amount': 1, 'token': ADDRESS})
```

## Vote

Creator methods:
```
# Create an vote (with a max. voting amount, and a candidate-resolution mechanism)
vote = xeta.vote.create(
    {'expires': TIMESTAMP, 'mechanism': 'candidate', 'maxAmount': 50, 'candidates': [ADDRESS, ADDRESS]},
    {'token': ADDRESS})
```

Participant methods:
```
# Submit a XETA-bid
vote.transfer({'amount': 5})

# Resolve a finished vote
vote.resolve()

# Claim proceeds (if mechanism is top:N)
vote.claim()
```

# Feedback & Contributions

We encourage contributions to this library. Please also join our social channels in case you have suggestions or require technical help.

[**Website**](https://xetareality.com)
[**App**](https://xeta.network)
[**Twitter**](https://twitter.com/XetaReality)
[**Telegram**](https://t.me/XetaReality)