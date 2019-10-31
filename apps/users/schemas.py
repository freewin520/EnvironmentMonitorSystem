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

UserAddSchema = AutoSchema([
    # token_field,
    coreapi.Field(
                "true_name",
                required=False,
                location="form", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="姓名",
            ),
    coreapi.Field(
                "tel",
                required=False,
                location="form", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="电话",
            ),
    coreapi.Field(
                "gender",
                required=False,
                location="form", #form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="性别",
            ),
    coreapi.Field(
                "status",
                required=False,
                location="form", #form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="状态",
            ),
    coreapi.Field(
                "address1",
                required=False,
                location="form", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="一级地址",
            ),
    coreapi.Field(
                "address2",
                required=False,
                location="form", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="二级地址",
            ),
    coreapi.Field(
                "describe",
                required=False,
                location="form", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="描述",
            ),
    coreapi.Field(
                "picture",
                required=False,
                location="form", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="头像",
            ),

])