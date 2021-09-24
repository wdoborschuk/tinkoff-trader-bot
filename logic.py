#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import tinvest as ti

SB_TOKEN = "t.TDZxZPlQ76Z2c840lsIDFc9eEAUuV0XMsTGomywxyHn9eZ76po34PXMPMOrib4gAJckiYRKDDiZzp79lCe33Fw"
TOKEN = "t.vq30T-9FrtNzfkaHpYwmQOdSly-EN4-hJUqDgFbNFRIK5XVNI0-91iVwF8ccyFXCjJQX0DtMhBTptn2I9FNVzA"

async def main():
    client = ti.AsyncClient(TOKEN)
    response = await client.get_portfolio()  # tinvest.PortfolioResponse
    print(response.payload)

    await client.close()

asyncio.run(main())