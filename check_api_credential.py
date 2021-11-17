#!/usr/bin/env python
from argparse import ArgumentParser
from fireblocks_sdk import FireblocksSDK


def get_client() -> FireblocksSDK:
    parser = ArgumentParser()
    parser.add_argument('private_key_path')
    parser.add_argument('api_key')
    args_ = parser.parse_args()
    with open(args_.private_key_path) as f:
        return FireblocksSDK(f.read(), args_.api_key)


if __name__ == "__main__":
    fireblocks = get_client()
    print(fireblocks.get_transactions_with_page_info())

