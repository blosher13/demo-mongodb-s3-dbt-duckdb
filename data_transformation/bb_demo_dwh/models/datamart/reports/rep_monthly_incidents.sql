{{config(
    materialized='external',
    location='s3://bb-s3-demobucket-215520152793-us-east-2-an/curated/reports/rep_monthly_incidents.parquet',
    format='parquet'
)}}

{% set statuses = ['Open', 'Closed'] %}

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
        strftime(incident_date, '%Y-%m') as incident_month,
        status as incident_status
    from tranformed_incidents

),
final as (

    select
        incident_month,
        -- count(incident_id) as total_incidents,
        -- count(case when incident_status = 'Open' then 1 end) as open_incidents,
        -- count(case when incident_status = 'Closed' then 1 end) as closed_incidents
        {% for status in statuses %}
            count(
                case when incident_status = '{{ status }}' 
                then incident_id end
                ) as {{ status }}_incidents{% if not loop.last %},{% endif %}
        {% endfor %}
    from intermediate
    group by incident_month
    order by incident_month desc

)
select * from final