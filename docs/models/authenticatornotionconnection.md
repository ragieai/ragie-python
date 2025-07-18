# AuthenticatorNotionConnection


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `provider`                                                           | *Literal["notion"]*                                                  | :heavy_check_mark:                                                   | N/A                                                                  |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `workspace_name`                                                     | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `user_email`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The email of the Notion account this is for                          |
| `credentials`                                                        | [models.AccessTokenCredentials](../models/accesstokencredentials.md) | :heavy_check_mark:                                                   | N/A                                                                  |