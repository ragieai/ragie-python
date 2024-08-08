# Entities
(*entities*)

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

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.entities.list_instructions()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |


### Response

**[List[models.Instruction]](../../models/.md)**
### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ErrorMessage | 401                 | application/json    |
| models.SDKError     | 4xx-5xx             | */*                 |

## create_instruction

Create a new instruction. Instructions are applied to documents as they are created or updated. The results of the instruction are stored as structured data in the schema defined by the `entity_schema` parameter. The `prompt` parameter is a natural language instruction which will be applied to documents. This feature is in beta and may change in the future.

### Example Usage

```python
import ragie
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.entities.create_instruction(request={
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
    "filter_": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.CreateInstructionParams](../../models/createinstructionparams.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |


### Response

**[models.Instruction](../../models/instruction.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## update_instruction

Update Instruction

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.entities.update_instruction(instruction_id="<INSTRUCTION_ID>", update_instruction_params={
    "active": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `instruction_id`                                                          | *str*                                                                     | :heavy_check_mark:                                                        | The ID of the instruction.                                                | <INSTRUCTION_ID>                                                          |
| `update_instruction_params`                                               | [models.UpdateInstructionParams](../../models/updateinstructionparams.md) | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |


### Response

**[models.Instruction](../../models/instruction.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## list_by_instruction

Get Instruction Extracted Entities

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.entities.list_by_instruction(request={
    "instruction_id": "<INSTRUCTION_ID>",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.ListEntitiesByInstructionRequest](../../models/listentitiesbyinstructionrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |


### Response

**[models.ListEntitiesByInstructionResponse](../../models/listentitiesbyinstructionresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

## list_by_document

Get Document Extracted Entities

### Example Usage

```python
from ragie import Ragie

s = Ragie(
    auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.entities.list_by_document(request={
    "document_id": "<DOCUMENT_ID>",
})

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.ListEntitiesByDocumentRequest](../../models/listentitiesbydocumentrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |


### Response

**[models.ListEntitiesByDocumentResponse](../../models/listentitiesbydocumentresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ErrorMessage        | 401                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
