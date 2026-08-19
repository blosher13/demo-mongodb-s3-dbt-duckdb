with source as (
    select * from {{ source('bb-mdb-democluster', 'care_plans') }}
),
renamed as (
    select
        _id             as care_plan_record_id,
        care_plan_id,
        student_id,
        condition,
        severity,
        plan_type,
        status,
        emergency_procedure,
        cast(created_date as timestamp) as created_date,
        cast(review_date as timestamp)  as review_date
    from source
)
select * from renamed