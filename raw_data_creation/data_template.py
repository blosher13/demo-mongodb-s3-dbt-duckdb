import random
import uuid
from datetime import datetime

from faker import Faker


fake = Faker("en_GB")


# ============================================================
# Generic generators
# ============================================================

def generate_id(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def generate_value(generator):
    """Generate a value from a list or registered generator."""

    if isinstance(generator, list):
        return random.choice(generator)

    return GENERATORS[generator]()


# ============================================================
# Controlled values
# ============================================================

SCHOOL_TYPES = [
    "Primary School",
    "Secondary School",
    "Academy",
]

STAFF_ROLES = [
    "Teacher",
    "First Aider",
    "Administrator",
    "School Nurse",
]

YEAR_GROUPS = [f"Year {i}" for i in range(1, 5)]

GENDERS = [
    "Male",
    "Female",
    "Non-binary",
]

RELATIONSHIP_TYPES = [
    "Mother",
    "Father",
    "Guardian",
]

CONTACT_METHODS = [
    "Email",
    "Phone",
    "SMS",
]

INCIDENT_TYPES = [
    "Injury",
    "Illness",
    "Accident",
    "Fall",
]

SEVERITIES = [
    "Low",
    "Moderate",
    "High",
]

MEDICATIONS = [
    "Salbutamol",
    "Paracetamol",
    "Antihistamine",
]

MEDICAL_CONDITIONS = [
    "Asthma",
    "Food Allergy",
    "Epilepsy",
]

QUALIFICATIONS = [
    "Paediatric First Aid",
    "First Aid at Work",
    "Mental Health First Aid",
]

LOCATIONS = [
    "Classroom",
    "Playground",
    "Sports Field",
    "Medical Room",
]

DOSAGES = [
    "1 tablet",
    "2 tablets",
    "2 puffs",
]

FREQUENCIES = [
    "Once daily",
    "Twice daily",
    "As required",
]

ADMINISTRATION_STATUSES = [
    "Administered",
    "Refused",
    "Not Required",
]


INVESTIGATION_STATUSES = [
    "Not Required",
    "In Progress",
    "Completed",
]


INCIDENT_STATUSES = [
    "Open",
    "Closed",
]

CARE_PLAN_TYPES = [
    "Healthcare Plan",
    "Emergency Plan",
]

CARE_PLAN_STATUSES = [
    "Active",
    "Expired",
]

# ============================================================
# Generator registry
# ============================================================

GENERATORS = {

    # Faker
    "email": fake.email,
    "phone": fake.phone_number,
    "address": fake.street_address,
    "city": fake.city,
    "postcode": fake.postcode,
    "name": fake.name,
    "first_name": fake.first_name,
    "last_name": fake.last_name,
    "text": lambda: fake.sentence(nb_words=10),
    "number": lambda: random.randint(1, 50),
    "boolean": lambda: random.choice([
        True,
        False,
    ]),

    "date": lambda: datetime.combine(
        fake.date_between(start_date="-2y", end_date="today"),
        datetime.min.time(),
    ),

    "datetime": lambda: fake.date_time_between(
        start_date="-2y",
        end_date="now",
    ),

    # Custom
    "generate_id": generate_id,
}


# ============================================================
# Schemas
# ============================================================

SCHOOLS_SCHEMA = {
    "school_id": "generate_id",
    "school_name": "name",
    "school_type": SCHOOL_TYPES,
    "address": "address",
    "city": "city",
    "postcode": "postcode",
    "phone": "phone",
    "email": "email",
}

STUDENTS_SCHEMA = {
    "student_id": "generate_id",
    "school_id": "reference",
    "first_name": "first_name",
    "last_name": "last_name",
    "date_of_birth": "date",
    "gender": GENDERS,
    "year_group": YEAR_GROUPS,

    # Parent/carer
    "parent_name": "name",
    "parent_relationship": RELATIONSHIP_TYPES,
    "parent_email": "email",
    "parent_phone": "phone",
}

STAFF_SCHEMA = {
    "staff_id": "generate_id",
    "school_id": "reference",
    "first_name": "first_name",
    "last_name": "last_name",
    "job_title": STAFF_ROLES,
    "email": "email",
    "phone": "phone",
    "qualification": QUALIFICATIONS,
    "qualification_expiry": "date",
}

INCIDENTS_SCHEMA = {
    "incident_id": "generate_id",
    "school_id": "reference",
    "student_id": "reference",
    "reported_by": ("reference", "staff_id"),
    "incident_type": INCIDENT_TYPES,
    "severity": SEVERITIES,
    "incident_date": "datetime",
    "location": LOCATIONS,
    "description": "text",
    "action_taken": "text",
    "witness_name": "name",
    "investigation_status": INVESTIGATION_STATUSES,
    "parent_notified": "boolean",
    "notification_method": CONTACT_METHODS,
    "status": INCIDENT_STATUSES,
}


MEDICATIONS_SCHEMA = {
    "medication_id": "generate_id",
    "student_id": "reference",
    "school_id": "reference",
    "medication_name": MEDICATIONS,
    "dosage": DOSAGES,
    "frequency": FREQUENCIES,
    "quantity_in_stock": "number",
    "expiry_date": "date",
    "last_administered": "datetime",
    "administered_by": ("reference", "staff_id"),
    "administration_status": ADMINISTRATION_STATUSES,
}


CARE_PLANS_SCHEMA = {
    "care_plan_id": "generate_id",
    "student_id": "reference",
    "condition": MEDICAL_CONDITIONS,
    "severity": SEVERITIES,
    "plan_type": CARE_PLAN_TYPES,
    "emergency_procedure": "text",
    "created_date": "date",
    "review_date": "date",
    "status": CARE_PLAN_STATUSES,
}


# ============================================================
# Schema registry
# ============================================================

SCHEMAS = {
    "schools": SCHOOLS_SCHEMA,
    "students": STUDENTS_SCHEMA,
    "staff": STAFF_SCHEMA,
    "incidents": INCIDENTS_SCHEMA,
    "medications": MEDICATIONS_SCHEMA,
    "care_plans": CARE_PLANS_SCHEMA,
}

