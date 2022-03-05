from brownie import network, accounts, config

LOCAL_BLOCKCHAIN_ENV = ["development", "test-ganache-local"]
FORKED_LOCAL_ENV = ["mainnet-fork"]


def get_account(index=None, id=None):
    # account[0]
    # account("env")
    # account("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENV
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        account = accounts[0]
        return account

    return accounts.add(config["wallets"]["from_key"])
