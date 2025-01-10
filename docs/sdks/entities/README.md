# Entities
(*entities*)

## Overview

### Available Operations

* [list_instructions](#list_instructions) - List Instructions
* [create_instruction](#create_instruction) - Create Instruction
* [update_instruction](#update_instruction) - Update Instruction
* [list_by_instruction](#list_by_instruction) - Get Instruction Extracted Entities
* [list_by_document](#list_by_document) - Get Document Extracted Entities

## list_instructions

List all instructions.

### Example Usage

```python
from ragie import Ragie

with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as ragie:

    res = ragie.entities.list_instructions()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Instruction]](../../models/.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ErrorMessage | 401, 402, 429       | application/json    |
| models.SDKError     | 4XX, 5XX            | \*/\*               |

## create_instruction

Create a new instruction. Instructions are applied to documents as they are created or updated. The results of the instruction are stored as structured data in the schema defined by the `entity_schema` parameter. The `prompt` parameter is a natural language instruction which will be applied to documents. This feature is in beta and may change in the future.

### Example Usage

```python
import ragie
from ragie import Ragie

with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as ragie:

    res = ragie.entities.create_instruction(request={
        "name": "Find all pizzas",
        "prompt": "Find all pizzas described in the text.",
        "entity_schema": {
            "additionalProperties": False,
            "properties": {
                "size": {
                    "enum": [
                        "small",
                        "medium",
                        "large",
                    ],
                    "type": "string",
                },
                "crust": {
                    "enum": [
                        "thin",
                        "thick",
                        "stuffed",
                    ],
                    "type": "string",
                },
                "sauce": {
                    "enum": [
                        "tomato",
                        "alfredo",
                        "pesto",
                    ],
                    "type": "string",
                },
                "cheese": {
                    "enum": [
                        "mozzarella",
                        "cheddar",
                        "parmesan",
                        "vegan",
                    ],
                    "type": "string",
                },
                "toppings": {
                    "items": {
                        "enum": [
                            "pepperoni",
                            "mushrooms",
                            "onions",
                            "sausage",
                            "bacon",
                            "extra cheese",
                            "black olives",
                            "green peppers",
                            "pineapple",
                            "spinach",
                        ],
                        "type": "string",
                    },
                    "type": "array",
                    "uniqueItems": True,
                },
                "extraInstructions": {
                    "type": "string",
                },
            },
            "required": [
                "size",
                "crust",
                "sauce",
                "cheese",
            ],
            "title": "Pizza",
            "type": "object",
        },
        "active": True,
        "scope": ragie.CreateInstructionParamsScope.CHUNK,
        "partition": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CreateInstructionParams](../../models/createinstructionparams.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.Instruction](../../models/instruction.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_instruction

Update Instruction

### Example Usage

```python
from ragie import Ragie

with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as ragie:

    res = ragie.entities.update_instruction(instruction_id="00000000-0000-0000-0000-000000000000", update_instruction_params={
        "active": True,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `instruction_id`                                                          | *str*                                                                     | :heavy_check_mark:                                                        | The ID of the instruction.                                                | 00000000-0000-0000-0000-000000000000                                      |
| `update_instruction_params`                                               | [models.UpdateInstructionParams](../../models/updateinstructionparams.md) | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[models.Instruction](../../models/instruction.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_by_instruction

Get Instruction Extracted Entities

### Example Usage

```python
from ragie import Ragie

with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as ragie:

    res = ragie.entities.list_by_instruction(request={
        "instruction_id": "00000000-0000-0000-0000-000000000000",
        "partition": "acme_customer_id",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.ListEntitiesByInstructionRequest](../../models/listentitiesbyinstructionrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ListEntitiesByInstructionResponse](../../models/listentitiesbyinstructionresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_by_document

Get Document Extracted Entities

### Example Usage

```python
from ragie import Ragie

with Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
) as ragie:

    res = ragie.entities.list_by_document(request={
        "document_id": "00000000-0000-0000-0000-000000000000",
        "partition": "acme_customer_id",
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.ListEntitiesByDocumentRequest](../../models/listentitiesbydocumentrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ListEntitiesByDocumentResponse](../../models/listentitiesbydocumentresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401, 402, 429              | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |