{{ config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/fct_incidents/fct_incidents.parquet',
    format='parquet'
) }}

with incidents as (

    select * from {{ ref('stg_incidents') }}

),

students as (

    select student_id, student_key from {{ ref('dim_students') }}

),

schools as (

    select school_id, school_key from {{ ref('dim_schools') }}

),

staff as (

    select staff_id, staff_key from {{ ref('dim_staff') }}

)

select
    incidents.incident_record_id  as incident_key,
    incidents.incident_id,
    students.student_key,
    schools.school_key,
    staff.staff_key                as reported_by_staff_key,
    incidents.incident_type,
    incidents.severity,
    incidents.status,
    incidents.investigation_status,
    incidents.location,
    incidents.description,
    incidents.action_taken,
    incidents.witness_name,
    incidents.parent_notified,
    incidents.notification_method,
    incidents.incident_date

from incidents
left join students on incidents.student_id            = students.student_id
left join schools  on incidents.school_id              = schools.school_id
left join staff    on incidents.reported_by_staff_id    = staff.staff_id
