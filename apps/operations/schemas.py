import coreapi
import coreschema
from rest_framework.schemas import AutoSchema, ManualSchema

token_field = coreapi.Field(
                name="Authorization",
                required=False,
                location="header",
                schema=coreschema.String(),
                description="格式：JWT 值",
        )
TokenSchema = AutoSchema([
                token_field
        ]
)

DoolApproveSchema = AutoSchema([
    # token_field,
    coreapi.Field(
                "door_id",
                required=False,
                location="query", #form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="门禁id",
            ),
])

DoorApproveTimeSchema = AutoSchema([
    coreapi.Field(
                "time_min",
                required=False,
                location="query", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="门禁申请时间min",
    ),
    coreapi.Field(
                "time_max",
                required=False,
                location="query", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="门禁申请时间max",
    ),
])