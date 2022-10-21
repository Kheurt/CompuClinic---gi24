from shared.serializer import enum_serializer

TYPES_PARAMETRE = (
    ('Taille', 'Taille'),
    ('Poids', 'Poids'),
    ('Température', 'Température'),
    ('Pression', 'Pression Sanguine'),
)

TYPES_SYMPTOME = (
    ('A', 'A'),
    ('B', 'B')
)

TYPE = (
        (0, 'Consultation'),
        (1, 'Suivi')
    )

LISTE_ENUM = {
    'TYPE_PARAMETRE': enum_serializer(TYPES_PARAMETRE),
    'TYPES_SYMPTOME': enum_serializer(TYPES_SYMPTOME),
    'TYPE': enum_serializer(TYPE),
}
TYPE_DE_PRELEVEMENT = (
    ('Nasopharynge','Nasopharynge'),
    ('Autre','Autre'),
)
INDICATION_DU_PRELEVEMENT = (
    ('Volontaire','Volontaire'),
    ('Controle','Controle'),
    ('Autre','Autre'),
)
RESULTAT_COVID = (
    ('En attente','En attente'),
    ('Presence de SARS Cov Ag','Presence de SARS Cov Ag'),
    ('Absence de SARS Cov Ag','Absence de SARS Cov Ag'),
    ('Indetermine','Indetermine'),
)