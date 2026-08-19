{{ config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/fct_medication_administrations/fct_medication_administrations.parquet',
    format='parquet'
) }}

with medications as (

    select * from {{ ref('stg_medications') }}

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
    medications.medication_record_id  as medication_administration_key,
    medications.medication_id,
    students.student_key,
    schools.school_key,
    staff.staff_key                    as administered_by_staff_key,
    medications.medication_name,
    medications.dosage,
    medications.frequency,
    medications.administration_status,
    medications.quantity_in_stock,
    medications.last_administered_at,
    medications.expiry_date

from medications
left join students on medications.student_id = students.student_id
left join schools  on medications.school_id  = schools.school_id
left join staff    on medications.staff_id   = staff.staff_id
