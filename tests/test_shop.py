from brownie import accounts, Shop
from scripts.deploy import deploy_merchant

ETH = 1e18
GWEI = 1e9


def test_deploy_merchant():
    merchant_account = accounts[0]
    try:
        shop = Shop.deploy({"from": merchant_account})
    except:
        assert False


def test_deploy_buyer():
    buyer = accounts[1]
    try:
        shop = Shop.deploy({"from": buyer})
        assert False
    except:
        assert True


def test_Pricing():
    shop = deploy_merchant()
    shop.Pricing(1e12)
    assert shop.price() == 1e12


def test_Pay():
    merchant_account = accounts[0]
    intial_balance = merchant_account.balance()
    shop = deploy_merchant()
    shop.Pricing(1 * ETH, {"from": merchant_account})

    txn = shop.Pay({"from": merchant_account, "value": 5 * ETH})
    txnCost = txn.gas_used * txn.gas_price

    assert(shop.balance() == intial_balance - merchant_account.balance()-txnCost)



def test_withdraw_merchant():
    merchant_account = accounts[0]
    shop = deploy_merchant()
    shop.Pricing(1 * ETH, {"from": merchant_account})
    shop.Pay({"from": merchant_account, "value": 5 * ETH})

    merchantPrevBalance = merchant_account.balance()
    contractPrevBalance = shop.balance()
    txn = shop.Withdraw({"from":merchant_account})
    txnCost = txn.gas_used * txn.gas_price
    assert(merchant_account.balance() == contractPrevBalance+merchantPrevBalance - txnCost)

def test_withdraw_buyer():
    merchant_account = accounts[0]
    buyer_account = accounts[1]
    shop = deploy_merchant()
    shop.Pricing(1 * ETH, {"from": merchant_account})
    shop.Pay({"from": buyer_account, "value": 5 * ETH})

    try:
        txn = shop.Withdraw({"from":buyer_account})
        assert(False)
    except:
        assert(True)
