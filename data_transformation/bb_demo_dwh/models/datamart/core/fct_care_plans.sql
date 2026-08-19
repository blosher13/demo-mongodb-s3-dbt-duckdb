{{ config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/fct_care_plans/fct_care_plans.parquet',
    format='parquet'
) }}

with care_plans as (

    select * from {{ ref('stg_care_plans') }}

),

students as (

    select student_id, student_key from {{ ref('dim_students') }}

)

select
    care_plans.care_plan_id as care_plan_key,
    care_plans.care_plan_id,
    students.student_key,
    care_plans.condition,
    care_plans.plan_type,
    care_plans.severity,
    care_plans.status,
    care_plans.emergency_procedure,
    care_plans.created_date,
    care_plans.review_date

from care_plans
left join students on care_plans.student_id = students.student_id
