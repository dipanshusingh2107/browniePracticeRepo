from brownie import accounts , Shop

ETH = 1e18
GWEI = 1e9


def deploy_merchant():
    merchant_account = accounts[0]
    shop = Shop.deploy({'from':merchant_account})
    assert(merchant_account == '0x66aB6D9362d4F35596279692F0251Db635165871')
    return shop

