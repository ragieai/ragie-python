# AuthenticatorSlackConnection


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `provider`                                                           | *Literal["slack"]*                                                   | :heavy_check_mark:                                                   | N/A                                                                  |
| `data`                                                               | [models.SlackData](../models/slackdata.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |
| `user_email`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The email of the Slack account this is for                           |
| `credentials`                                                        | [models.AccessTokenCredentials](../models/accesstokencredentials.md) | :heavy_check_mark:                                                   | N/A                                                                  |