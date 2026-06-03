# CharacterIndexLocation

Location within linear text using zero-based character offsets.


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `location_type`                        | *Optional[Literal["character_index"]]* | :heavy_minus_sign:                     | N/A                                    |
| `start_char_index`                     | *int*                                  | :heavy_check_mark:                     | Start character index (inclusive)      |
| `end_char_index`                       | *int*                                  | :heavy_check_mark:                     | End character index (exclusive)        |