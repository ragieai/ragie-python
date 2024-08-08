<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.documents.list(request={
    "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break

```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from ragie import Ragie

async def main():
    s = Ragie(
        auth="<YOUR_BEARER_TOKEN_HERE>",
    )
    res = await s.documents.list_async(request={
        "filter_": "{\"department\":{\"$in\":[\"sales\",\"marketing\"]}}",
    })
    if res is not None:
        while True:
            # handle items
    
            res = res.Next()
            if res is None:
                break

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->