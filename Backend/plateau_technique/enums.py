from consultation.enum import TYPES_PARAMETRE
from shared.serializer import enum_serializer

TYPE_EQUIPEMENT = (
    ('Équipement d\'ambulance','Équipement d\'ambulance'),
    ('Équipement d\'accueil','Équipement d\'accueil'),
    ('Équipement de consultation','Équipement de consultation'),
    ('Équipement d\'urgence','Équipement d\'urgence'),
    ('Équipement d\'hospitalisation','Équipement d\'hospitalisation'),
    ('Équipement d\'analyses biomedicales','Équipement d\'analyses biomedicales'),
    ('Équipement d\'anatomie pathologique','Équipement d\'anatomie pathologique'),
    ('Équipement d\'imagerie medicale','Équipement d\'imagerie medicale'),
    ('Équipement d\'explorations fonctionnelles','Équipement d\'explorations fonctionnelles'),
    ('Équipement d\'endoscopie','Équipement d\'endoscopie'),
    ('Équipement d\'electrodiagnositc','Équipement d\'electrodiagnositc'),
    ('Équipement de chirugie','Équipement de chirugie'),
    ('Équipement d\'anesthesie','Équipement d\'anesthesie'),
    ('Équipement obstetrical','Équipement obstetrical'),
    ('Équipement de sterilisation','Équipement de sterilisation'),
    ('Équipement de reanimation','Équipement de reanimation'),
    ('Équipement de kinesitherapie','Équipement de kinesitherapie'),
    ('Équipement de morgue','Équipement de morgue'),
    ('autres Équipements','autres Équipements'),
    ('Livres de medecine','Livres de medecine')
)

TYPE_SERVICE = (
    ('DIRECTION MEDICALE','Direction médicale'),
    ('DIRECTION PARAMÉDICALE','Direction paramédicale'),
    ('SERVICE URGENCES','Service des Urgences'),
    ('SERVICE CONSULTATIONS  Externes & Soins ambulatoires','Service des Consultations  Externes & Soins ambulatoires'),
    ('SERVICE HOSPITALISATION','SERVICE DES HOSPITALISATION'),
    ('SERVICE BLOC TECHNIQUE','SERVICE BLOC TECHNIQUE'),
    ('SERVICE ANESTHESIE-REANIMATION','SERVICE D ANESTHESIE-REANIMATION'),
    ('SERVICE LABORATOIRE BIOMEDICAL','SERVICE DE LABORATOIRE BIOMEDICAL'),
    ('SERVICE IMAGERIE MEDICALE','SERVICE D IMAGERIE MEDICALE'),
    ('SERVICE PHYSIOTHERAPIE REEDUCATION FONCTIONNELLE','SERVICE DE PHYSIOTHERAPIE REEDUCATION FONCTIONNELLE'),
    ('SERVICE RADIOTHERAPIE','SERVICE DE RADIOTHERAPIE')
)

CLASSES = (
    ('A', "A"),
    ('B', 'B'),
    ('C', 'C'),
)

SPECIALITES =(
    ('URGENCE PREADMISION','Unité de Préadmission'),
    ('URGENCE MED','Unité des urgences médicales'),
    ('URGENCE CHIR','Unité des urgences chirurgicales'),
    ('CONSULT MED','Unité des Consultations médicales des explorations fonctionnelles'),
    ('CONSULT CHIR','Unité des Consultations chirurgicales'),
    ('GYN-OBST','Unité des Consultations gynéco-obstétricales'),
    ('CONSULT STOMATO','Unité des Consultations stomatologiques'),
    ('CONSULT OPHTALMO','Unité des Consultations ophtalmologiques'),
    ('CONSULT ORL','Unité des Consultations otorhinolaryngologiques '),
    ('HOSPI MED','Unité d hospitalisation médicale'),
    ('HOSPI CHIR','Unité d hospitalisation chirurgicale '),
    ('HOSPI GYN','Unité d hospitalisation Gynéco-obstétricale '),
    ('HOSPI PEDIA','Unité d hospitalisation pédiatrique '),
    ('HOSPI PEDIA','Unité d hospitalisation VIP '),
    ('HOSPI PSY','Unité d hospitalisation psychiatrique '),
    ('HOSPI REHABIL','Unité d hospitalisation réhabilitation '),
    ('HOSPI REA','Unité d hospitalisation Réanimation '),
    ('HOSPI HEMODIA','Unité d hospitalisation Hémodialyse '),
    ('BLOC OP','Unité Bloc opératoire ',),
    ('BLOC STERI','Unité de Stérilisation centrale '),
    ('BLOC SPI','Unité de Stérilisation centrale '),
    ('BLOC OBST','Unité Bloc obstétrical '),
    ('ANESTH','Unité d anesthésie '),
    ('HOSPI REA','Unité de réanimation '),
    ('LAB ANALYSES','Unité d analyses biomédicales courantes '),
    ('LAB TRANSFUSION','Unité de Tansfusion sanguine '),
    ('LAB BIOMOLECULAIRE','Unité de biologie moléculaire '),
    ('IMAG RADIO','Unité de radiologie conventionnelle'),
    ('IMAG SCANNER','Unité  Scanner '),
    ('IMAG IRM','Unité IRM '),
    ('IMAG ECHO','Unité d échographie '),
    ('IMAG GAMMA','Unité Gamma camera '),
    ('ANAPATH HISTO','Unité d histopathologie '),
    ('ANAPATH MEDICO LEGAL','Unité de médecine légale '),
    ('PHYSIOTHER PHYSIO','Unité de Physiothérapie '),
    ('PHYSIOTHER KINE','Unité de Kinésithérapie '),
    ('PHYSIOTHER ERGOT','Unité d ergothérapie '),
    ('RADIOTHER EXT','Unité de radiothérapie externe '),
    ('RADIOTHER CONTACT','Unité de radiothérapie de contact '),
    ('RADIOTHER ISOTOPE','Unité de radiothérapie isotopique ')
)

TYPE_MATERIEL = (
    ('Informatique', 'Informatique'),
    ('Medical', 'Médical'),
    ('Mobilier', 'Mobilier'),
    ('Electronique', 'Electronique'),
    ('Bureau', 'Bureau'),
)

LISTE_ENUM = {
    'TYPE_EQUIPEMENT': enum_serializer(TYPE_EQUIPEMENT),
    'CLASSES': enum_serializer(CLASSES),
    'TYPE_MATERIEL': enum_serializer(TYPE_MATERIEL),
}