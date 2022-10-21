from shared.serializer import enum_serializer

TYPE_MEDECIN = (
    ('G', 'Généraliste'),
    ('S', 'Spécialiste'),
)

ETAT_CIVIL = (
    ('MR', "M."),
    ('MME', 'Mme.'),
    ('MLLE', 'Mlle.')
)

SCHOOL_LEVEL = (
    ('BEPC', 'BEPC'),
    ('BAC', 'BAC'),
    ('BAC+1', 'BAC+1'),
    ('BAC+2', 'BAC+2'),
    ('BAC+3', 'BAC+3'),
    ('BAC+4', 'BAC+4'),
    ('BAC+5', 'BAC+5'),
    ('BAC+6', 'BAC+6'),
    ('BAC+7', 'BAC+7'),
)


TYPE_PERSONNEL = (
    ('Medecin', "Médecin"),
    ('Caissier', "Caissier"),
    ('Secretaire', "Sécrétaire"),
    ('Infirmer', "Infirmier"),
    ('Laborantin', 'Laborantin'),
    ('Stagiaire', 'Stagiaire')
)

PERIOD_TYPE = (
    ('repeat', 'Répété'),
    ('fixed', 'Fixé'),
)

WEEK_DAYS = (
    (0, 'lundi'),
    (1, 'mardi'),
    (2, 'mercredi'),
    (3, 'jeudi'),
    (4, 'vendredi'),
    (5, 'samedi'),
    (6, 'dimanche'),
)

LISTE_ENUM = {
    'TYPE_MEDECIN': enum_serializer(TYPE_MEDECIN),
    'ETAT_CIVIL': enum_serializer(ETAT_CIVIL),
    'SCHOOL_LEVEL': enum_serializer(SCHOOL_LEVEL),
    'TYPE_PERSONNEL': enum_serializer(TYPE_PERSONNEL),
    'PERIOD_TYPE': enum_serializer(PERIOD_TYPE),
    'WEEK_DAYS': enum_serializer(WEEK_DAYS),
}