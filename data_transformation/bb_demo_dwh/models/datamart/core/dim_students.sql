{{ config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/dim_students/dim_students.parquet',
    format='parquet'
) }}

with students as (

    select * from {{ ref('stg_students') }}

),

schools as (

    select school_id, school_key from {{ ref('dim_schools') }}

)

select
    students.student_id as student_key,
    students.student_id,
    schools.school_key,
    students.first_name,
    students.last_name,
    students.date_of_birth,
    students.gender,
    students.year_group,
    students.parent_name,
    students.parent_email,
    students.parent_phone,
    students.parent_relationship

from students
left join schools on students.school_id = schools.school_id
