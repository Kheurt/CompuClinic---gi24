from shared.serializer import enum_serializer

TYPE_PATIENT = (
    ('Externe', 'Externe'), 
    ('Interne', 'Interne'),
)

TYPE_RELIGION = (
    ('Chrétien', 'Chrétien'),
    ('Musulman', 'Musulman'),
    ('Boudiste', 'Boudiste'),
    ('Athée', 'Athée'),
    ('Animiste', 'Animiste')
)

TYPE_GROUP_SANGUIN = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)

LISTE_ENUM = {
    'TYPE_RELIGION': enum_serializer(TYPE_RELIGION),
    'TYPE_PATIENT': enum_serializer(TYPE_PATIENT),
    'TYPE_GROUPE_SANGUIN': enum_serializer(TYPE_GROUP_SANGUIN),
}