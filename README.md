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

# Generate and init a keypair
publicKey, privateKey = xeta.wallet.generateKeypair()
xeta.wallet.init(publicKey, privateKey)
```

# Interface

The interface methods allow to interact with storage nodes for read-only functionality. Using these methods, you could build a similar frontend app like our [**network explorer**](https://xeta.network). Interface requests are free, but rate-limited and should allow for "regular" usage. Please contact us at developers@xetareality.com if you would like to have dedicated limits.

## Transaction

```
xeta.transaction.poll(hash=hash, interval=number, timeout=number)
xeta.transaction.read(hash=hash)
xeta.transaction.list(hashes=[hash])
xeta.transaction.scanSenderCreated(sender=address)
xeta.transaction.scanPeriodCreated(period=period)
```

## Transfer

```
xeta.transfer.read(hash=hash)
xeta.transfer.list(hashes=[hash])
xeta.transfer.scanSenderCreated(sender=address)
xeta.transfer.scanFromCreated(fromAddress=address)
xeta.transfer.scanToCreated(to=address)
xeta.transfer.scanTokenCreated(token=token)
xeta.transfer.scanFromTokenCreated(fromAddress=address, token=token)
xeta.transfer.scanToTokenCreated(to=address, token=token)
```

## Token

```
xeta.token.read(address=token)
xeta.token.list(addresses=[token])
xeta.token.scanCreatorCreated(creator=address)
xeta.token.scanNameCreated(name=string)
xeta.token.scanSymbolCreated(symbol=string)
xeta.token.scanOwnerCreated(owner=address)
xeta.token.scanContentCreated(content=hash)
xeta.token.scanOwnerCategoryCreated(owner=address, category=string)
xeta.token.scanCreatorCategoryCreated(creator=address, category=string)
```

## Pool

```
xeta.pool.instance(address=pool)
xeta.pool.read(address=pool)
xeta.pool.list(addresses=[pool])
xeta.pool.scanTokenProgramCreated(token=token, program=string)
xeta.pool.scanNameCreated(name=string)
xeta.pool.scanCreatorCreated(creator=address)
```

## Account

```
xeta.account.read(address=address)
```

## Allowance

```
xeta.allowance.read(hash=hash)
xeta.allowance.list(hashes=[hash])
xeta.allowance.readAddressSpenderToken(address=address, spender=address, token=token)
xeta.allowance.scanAddressCreated(address=address)
xeta.allowance.scanSpenderCreated(spender=address)
```

## Balance

```
xeta.balance.read(hash=hash)
xeta.balance.list(hashes=[hash])
xeta.balance.readAddressToken(address=address, token=token)
xeta.balance.scanAddressAmount(address=address)
xeta.balance.scanTokenAmount(token=token)
```

## Candle

```
xeta.candle.read(interval=interval, token=token, time=time)
xeta.candle.scanIntervalTokenTime(interval=interval, token=token)
xeta.candle.scanIntervalTimeTurnover(interval=interval)
xeta.candle.scanIntervalTimeChange(interval=interval)
```

## Claim

```
xeta.claim.read(hash=hash)
xeta.claim.list(hashes=[hash])
xeta.claim.scanHolderCategoryCreated(holder=address, category=string)
xeta.claim.scanIssuerCategoryCreated(issuer=address, category=string)
xeta.claim.scanIssuerAnswer(issuer=address)
xeta.claim.scanIssuerNumber(issuer=address)
xeta.claim.scanIssuerTokenAmount(issuer=address)
xeta.claim.scanIssuerXetaAmount(issuer=address)
xeta.claim.scanIssuerCreated(issuer=address)
xeta.claim.scanHolderCreated(holder=address)
xeta.claim.scanIssuerTokenCreated(issuer=address, token=token)
xeta.claim.scanHolderTokenCreated(holder=address, token=token)
xeta.claim.scanIssuerHolder(issuer=address, holder=address)
xeta.claim.scanIssuerHolderToken(issuer=address, holder=address, token=token)
```

## Registry

```
xeta.registry.read(hash=hash)
xeta.registry.list(hashes=[hash])
xeta.registry.scanContentCreated(content=string)
xeta.registry.scanFingerprintCreated(fingerprint=string)
xeta.registry.scanClusterCreated(cluster=string)
```

## Search

```
xeta.search.query(query=string)
```

## Statistic

```
xeta.statistic.read(key=key, time=time)
xeta.statistic.scan(key=key)
```

## Wallet

```
xeta.wallet.init(publicKey=hash, privateKey=hash)
xeta.wallet.connect(account=string, secret=string, unsafe=boolean, create=boolean)
xeta.credentials.sign(account=string, secret=string, tx=transaction)
```

# Modules

Modules are wrapper methods that submit transactions to the network endpoint. Fees for methods are fixed and most recent fees can be found on [docs.xetareality.com](https://docs.xetareality.com). 


## Transfer

```
xeta.transfer.create(to=address, token=token, amount=amount, fromAddress=address)
```

## Token

```
xeta.token.create(name=string, description=string, links=[string], meta=object, icon=url, owner=address, frozen=boolean, category=string, object=url, mime=string, content=string)
xeta.token.create(name=string, symbol=string, supply=amount, reserve=amount, description=string, links=[string], meta=object, icon=url)
```

## Pool

For pool creation, it is recommended to use the program-specific methods (which are wrappers around this method). Available pool programs are auction, launch, lock, loot, lottery, royalty, staking, swap, vote.

```
xeta.pool.create(token=token, program=string, expires=timestamp)
```

## Claim
```
xeta.claim.create(owner=address, token=token, tokenAmount=amount, expires=timestamp)
xeta.claim.update(claim=claim, tokenAmount=amount)
xeta.claim.transfer(claim=claim, to=address)
xeta.claim.resolve(claim=claim)
```

## Account

```
xeta.account.update(name=string, description=string, links=[string], meta=object, icon=url, category=string)
```

## Allowance

```
xeta.allowance.update(token=token, spender=spender, amount=amount)
```

## Transaction
Approx. 10 instructions can be batched into one request. The exact number depends on reads & writes, and sub-calls made by each instruction. It is required that all instructions have the tx=False flag, to be returned as instruction object. Batch instructions are processed atomically, meaning that if one instruction fails, the transaction throws an error and no instruction is processed.

```
xeta.transaction.submit([
    xeta.transfer.create(to=address, token=token, amount=amount, tx=False),
    xeta.transfer.create(to=address, token=token, amount=amount, tx=False),
    xeta.token.create(name=string, symbol=string, supply=amount),
    xeta.token.create(name=string),
    xeta.token.create(name=string),
])
```

# Programs

Pools are based on programs, which are pre-written smart contracts on Xeta. For further details on individual functionalities or requirements check out the [Xeta Reality Docs](https://docs.xetareality.com). To get the pool object from pool-address, use the xeta.pool.get interface method.

## Auction

```
# Creator methods:
auction = xeta.pool.create(program='auction', token=token, expires=timestamp, xetaTarget=amount, xetaLimit=amount)
auction.deposit(amount=amount)
auction.close()

# Participant methods:
auction.transfer(amount=amount)
auction.resolve()
auction.cancel()
```

## Launch

```
# Creator methods:
launch = xeta.pool.create(program='launch', token=token, expires=timestamp, xetaTarget=amount, xetaLimit=amount)
launch.deposit(amount=amount)
launch.withdraw(claim=claim)
launch.close()

# Participant methods:
launch.resolve()
launch.transfer(amount=amount)
launch.swap(amount=amount)
launch.claim(claim=claim)
```

## Lending

```
# Creator methods:
lending = xeta.pool.create(program='lending', token=token)
lending.deposit(amount=amount)
lending.withdraw(claim=claim)

# Participant methods:
lending.liquidate(claim=claim)
lending.transfer(amount=amount, collateralization=number)
lending.settle(claim=claim)
```

## Lock

```
# Creator methods:
lock = xeta.pool.create(program='lock', token=token, expires=timestamp)

# Participant methods:
lock.transfer(amount=amount, unlocks=timestamp, address=address)
lock.claim(claim=claim)
```

## Loot

```
# Creator methods:
loot = xeta.pool.create(program='loot', token=token, probability=number, minAmount=amount, maxAmount=amount)
loot.deposit(token=token)
loot.withdraw(claim=claim)
loot.clear()

# Participant methods:
loot.transfer(amount=amount)
```

## Lottery

```
# Creator methods:
lottery = xeta.pool.create(program='lottery', token=token, expires=timestamp, claimsLimit=integer, transfersLimit=integer)
lottery.deposit(amount=amount)
lottery.withdraw(claim=claim)
lottery.close()
lottery.clear()

# Participant methods:
lottery.transfer(amount=amount)
lottery.claim(claim=claim)
lottery.resolve()
```

## Royalty

```
# Creator methods:
royalty = xeta.pool.create(program='royalty', token=token, rate=number)
royalty.deposit(amount=amount)
royalty.withdraw(claim=claim)
royalty.close()

# Participant methods:
royalty.transfer(token=token)
royalty.claim(token=token)
```

## Staking

```
# Creator methods:
staking = xeta.pool.create(program='staking', token=token, rate=number, percentage=number, minTime=integer, maxTime=integer, minAmount=amount, maxAmount=amount)
staking.deposit(amount=amount)
staking.withdraw(claim=claim)

# Participate methods:
staking.transfer(amount=amount, unlocks=timestamp)
staking.claim(claim=claim)
```

## Swap

Swap pools are automatically created for all fungible tokens, with the same pool-address as the token-address.

```
# Liquidity provider methods:
swap.deposit(tokenAmount=amount, xetaAmount=amount, unlocks=timestamp)
swap.withdraw(claim=claim, percentage=number)

# Participant methods:
swap.transfer(token=token, amount=amount)
```

## Vote

```
# Creator methods:
vote = xeta.pool.create(program='vote', token=token, expires=timestamp, mechanism=string, maxAmount=amount, candidates=[string])
xeta.vote.oracle(answer=answer)

# Participant methods:
vote.transfer(amount=amount, answer=string, number=number)
vote.resolve()
vote.claim(claim=claim)
```

# Feedback & Contributions

We encourage contributions to this library. Please also join our social channels in case you have suggestions or require technical help.

[**Website**](https://xetareality.com)
[**App**](https://xeta.network)
[**Twitter**](https://twitter.com/XetaReality)
[**Telegram**](https://t.me/XetaReality)