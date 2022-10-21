from shared.serializer import enum_serializer


RUBRIQUES = (
    ('MG-CO', 'Consultation par médecin généraliste'),
    ("MG-CRV", 'Consultation sur Rendez-vous par médecin généraliste'),
    ('MS-CO', 'Consultation par médecin spécialiste'),
    ("MS-CRV", 'Consultation sur Rendez-vous par médecin spécialiste'),
)

PRESTATIONS = (
    ('Q-CONSULT', 'Consultation'),
    ('Q-EXAM', 'Examen'),
    ('Q-PHARMA', 'Pharmacie'),
    ('Q-SA', 'Q-SA'),
    ('Q-SI', 'Q-SI'),
    ('Q-DIV', 'Q-DIV'),
    ('Q-FD', 'Q-FD'),
)


LISTE_ENUM = {
    'RUBRIQUES': enum_serializer(RUBRIQUES),
    'PRESTATIONS': enum_serializer(PRESTATIONS)
}
