{{ config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/dim_staff/dim_staff.parquet',
    format='parquet'
) }}
with staff as (

    select * from {{ ref('stg_staff') }}

),

schools as (

    select school_id, school_key from {{ ref('dim_schools') }}

)

select
    staff.staff_id as staff_key,
    staff.staff_id,
    schools.school_key,
    staff.first_name,
    staff.last_name,
    staff.email,
    staff.phone,
    staff.job_title,
    staff.qualification,
    staff.qualification_expiry

from staff
left join schools on staff.school_id = schools.school_id
