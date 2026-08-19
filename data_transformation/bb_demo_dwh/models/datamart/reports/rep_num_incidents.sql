{{config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/reports/rep_total_num_incidents.parquet',
    format='parquet'
)}}

with tranformed_incidents as (

    select
        incident_key,
        incident_id,
        student_key,
        school_key,
        reported_by_staff_key,
        incident_type,
        severity,
        status,
        investigation_status,
        location,
        description,
        action_taken,
        witness_name,
        parent_notified,
        notification_method,
        incident_date

    from {{ ref('fct_incidents') }}

),
intermediate as (

    select
        incident_id,
        strftime(incident_date, '%Y') as incident_year
    from tranformed_incidents

),
final as (

    select
        incident_year,
        count(incident_id) as total_incidents,
    from intermediate
    group by incident_year
    order by incident_year desc

)
select * from final