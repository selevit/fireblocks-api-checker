# Fireblocks API credentials checker

The tool lets SRE check if fireblocks credentials are valid, without revealing them to devs.

## Installation

Ensure that you have python 3 in your setup.

```
python3 -m venv ./venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
. venv/bin/activate
./check_api_credential.py <path_to_fb_rsa_private_key> <api_key>
```

### Example

```
./check_api_credential.py ../viewer_key.pem d2419d05-829a-4a3c-86af-e10ee2043dd3
```

The API key above is not real.

