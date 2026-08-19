
{{config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/reports/rep_num_medication_not_required.parquet',
    format='parquet'
)}}

with tranformed_medication_administrations as (

select
    medication_administration_key,
    medication_id,
    student_key,
    school_key,
    administered_by_staff_key,
    medication_name,
    dosage,
    frequency,
    administration_status,
    quantity_in_stock,
    last_administered_at,
    expiry_date

    from {{ ref('fct_medication_administrations') }}

),
intermediate as (

    select
        medication_id,
        quantity_in_stock,
        strftime(incident_date, '%Y') as year
    from tranformed_incidents
    where adminstration_status = 'Not Required'

),
final as (

    select
        year,
        count(medication_id) as number_of_medications_not_required,
        sum(quantity_in_stock) as total_quantity_not_required,
    from intermediate
    group by year
    order by year desc

)
select * from final