from brownie import OurToken
from web3 import Web3
from scripts.helpful_scripts import get_account


def deploy():
    account = get_account()
    print(f"[+] Using account: {account}")
    _initialSupply = Web3.toWei(1000, "ether")
    ourtoken = OurToken.deploy(_initialSupply, {"from": account})
    print(f"[+] {ourtoken.name()}")


def main():
    deploy()
