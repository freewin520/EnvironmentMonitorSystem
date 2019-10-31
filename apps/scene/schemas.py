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

AlarmListSchema = AutoSchema([
    # token_field,
    # coreapi.Field(
    #             "alarm_id",
    #             required=False,
    #             location="query", #form
    #             schema=coreschema.String(),
    #             # schema=coreschema.String(),
    #             description="警告id",
    #         ),
    coreapi.Field(
                "am_type_id",
                required=False,
                location="form", #form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="告警类型",
            ),
    coreapi.Field(
                "am_deal_detail",
                required=False,
                location="form", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="处理说明",
            )
    ])

# 单行处理
AlarmProcessSchema = AutoSchema([
    coreapi.Field(
                "am_id",
                required=False,
                location="form",
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="单行处理",
            ),
    coreapi.Field(
                "am_deal_detail",
                required=False,
                location="form",
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="处理说明",
            )

    ])

# 单行审批
AlarmCheckSchema = AutoSchema([
    coreapi.Field(
                "am_id",
                required=False,
                location="form",
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="单行处理",
            ),
    coreapi.Field(
                "am_audit_feedback",
                required=False,
                location="form",
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="审核反馈",
            ),
    coreapi.Field(
                "am_status",
                required=False,
                location="form",
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="处理状态",
            ),


    ])

# 多行审批
AlarmBatchCheckSchema = AutoSchema([
    coreapi.Field(
                "am_type_id",
                required=False,
                location="form", #form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="告警类型",
            ),
    coreapi.Field(
                "am_audit_feedback",
                required=False,
                location="form", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="处理说明",
            ),
    coreapi.Field(
                "am_status",
                required=False,
                location="form", #form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="处理说明",
            )
    ])

# 警告数量统计
AlarmNumStaticSchema = AutoSchema([
    coreapi.Field(
                "time_min",
                required=False,
                location="query", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="告警最小开始时间",
            ),
    coreapi.Field(
                "time_max",
                required=False,
                location="query", #form
                schema=coreschema.String(),
                # schema=coreschema.String(),
                description="告警最大开始时间",
            )
])

