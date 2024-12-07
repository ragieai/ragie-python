<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from ragie import Ragie

with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.documents.create(request={
        "file": {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    })

    if res is not None:
        # handle response
        pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from ragie import Ragie

async def main():
    async with Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as s:
        res = await s.documents.create_async(request={
            "file": {
                "file_name": "example.file",
                "content": open("example.file", "rb"),
            },
        })

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->