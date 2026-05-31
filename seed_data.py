"""
Run this script to populate the database with 100+ doctors.
Usage:  python seed_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medilink.settings')
django.setup()

from doctors.models import Doctor

Doctor.objects.all().delete()

# Color themes per specialization
CARD = {
    'Cardiologist':      ('&#10084;&#65039;',                        '#FAECE7', '#D85A30'),
    'Dermatologist':     ('&#129332;',                               '#E1F5EE', '#0F6E56'),
    'General Physician': ('&#128104;&#8205;&#9877;&#65039;',         '#E6F1FB', '#185FA5'),
    'Orthopedic':        ('&#129460;',                               '#FAEEDA', '#BA7517'),
    'Eye Specialist':    ('&#128065;&#65039;',                       '#EEEDFE', '#534AB7'),
    'Neurologist':       ('&#129504;',                               '#FDE8F5', '#A0359A'),
    'Pediatrician':      ('&#128118;',                               '#E8F8E8', '#2E7D32'),
    'Gynecologist':      ('&#127801;',                               '#FCE4EC', '#C2185B'),
    'Dentist':           ('&#129998;',                               '#E3F2FD', '#1565C0'),
    'ENT Specialist':    ('&#128066;',                               '#FFF8E1', '#F57F17'),
    'Psychiatrist':      ('&#129488;',                               '#F3E5F5', '#6A1B9A'),
    'Urologist':         ('&#128167;',                               '#E0F7FA', '#00695C'),
    'Gastroenterologist':('&#129745;',                               '#FBE9E7', '#BF360C'),
    'Pulmonologist':     ('&#129738;',                               '#E8EAF6', '#283593'),
    'Endocrinologist':   ('&#129527;',                               '#F9FBE7', '#827717'),
}

KW = {
    'Cardiologist':       ['heart','chest','cardiac','breath','shortness','pressure','pulse','palpitation','angina'],
    'Dermatologist':      ['skin','rash','itch','acne','allergy','pimple','eczema','psoriasis','fungal','hair','nail'],
    'General Physician':  ['fever','cold','cough','headache','body pain','vomit','flu','general','weakness','fatigue','diarrhea'],
    'Orthopedic':         ['bone','joint','knee','fracture','arthritis','back','shoulder','spine','walk','hip','ankle','wrist'],
    'Eye Specialist':     ['eye','vision','blur','glasses','glaucoma','cataract','sight','lens','redness','tears','cornea'],
    'Neurologist':        ['brain','nerve','seizure','migraine','stroke','memory','paralysis','tremor','numbness','headache','dizzy'],
    'Pediatrician':       ['child','baby','infant','kids','growth','vaccination','pediatric','newborn','toddler','fever child'],
    'Gynecologist':       ['pregnancy','period','menstrual','women','uterus','ovary','delivery','gynec','hormones','pcos'],
    'Dentist':            ['teeth','tooth','gum','cavity','dental','braces','root canal','wisdom','jaw','mouth','filling'],
    'ENT Specialist':     ['ear','nose','throat','hearing','tonsil','sinus','nasal','snoring','voice','swallowing','ent'],
    'Psychiatrist':       ['anxiety','depression','stress','mental','sleep','panic','phobia','ocd','bipolar','schizophrenia'],
    'Urologist':          ['urine','kidney','bladder','prostate','urinary','stone','uti','incontinence','urology'],
    'Gastroenterologist': ['stomach','liver','abdomen','constipation','acidity','ulcer','ibs','hepatitis','gastro','nausea'],
    'Pulmonologist':      ['lung','asthma','breathing','chest pain','bronchitis','tb','pneumonia','oxygen','respiratory','copd'],
    'Endocrinologist':    ['diabetes','thyroid','sugar','hormones','insulin','obesity','weight','metabolic','adrenal','pituitary'],
}

AVAIL = [
    'Mon-Fri, 9AM-5PM','Mon-Sat, 10AM-4PM','Mon-Fri, 8AM-6PM','Tue-Sat, 9AM-3PM',
    'Mon-Thu, 10AM-4PM','Mon-Sat, 8AM-8PM','Mon-Fri, 11AM-5PM','Sat-Wed, 9AM-1PM',
    'Mon-Fri, 2PM-8PM','Mon-Sun, 9AM-2PM','Wed-Sun, 10AM-6PM','Mon-Fri, 8AM-2PM',
]

doctors = [
    # ── CARDIOLOGISTS ──────────────────────────────────────────────
    ('Dr. Ahmed Raza',        'Cardiologist', 12, 'DHA, Lahore',           'City Cardiac Hospital',        '042-1112223330'),
    ('Dr. Anum Hassan',       'Cardiologist', 14, 'Defence, Lahore',       'Heart Care Institute',         '042-1112223331'),
    ('Dr. Tariq Mehmood',     'Cardiologist', 18, 'Gulberg, Lahore',       'Punjab Heart Centre',          '042-1112223332'),
    ('Dr. Zainab Qureshi',    'Cardiologist', 9,  'Model Town, Lahore',    'Cardio Life Clinic',           '042-1112223333'),
    ('Dr. Kamran Siddiqui',   'Cardiologist', 22, 'Cantt, Lahore',         'Armed Forces Cardiac Centre',  '042-1112223334'),
    ('Dr. Nadia Farooq',      'Cardiologist', 11, 'Bahria Town, Lahore',   'Bahria Heart Hospital',        '042-1112223335'),
    ('Dr. Imran Butt',        'Cardiologist', 7,  'Johar Town, Lahore',    'Johar Cardio Clinic',          '042-1112223336'),
    ('Dr. Shahida Parveen',   'Cardiologist', 16, 'Wapda Town, Lahore',    'Wapda Cardiac Centre',         '042-1112223337'),

    # ── DERMATOLOGISTS ─────────────────────────────────────────────
    ('Dr. Sara Khan',         'Dermatologist', 8,  'Gulberg, Lahore',      'Skin Care Center',             '042-2223334440'),
    ('Dr. Hira Malik',        'Dermatologist', 11, 'DHA, Lahore',          'Advanced Dermatology',         '042-2223334441'),
    ('Dr. Ayesha Noor',       'Dermatologist', 6,  'Model Town, Lahore',   'Glow Skin Clinic',             '042-2223334442'),
    ('Dr. Sana Riaz',         'Dermatologist', 13, 'Cantt, Lahore',        'Derm & Aesthetics',            '042-2223334443'),
    ('Dr. Omer Sheikh',       'Dermatologist', 9,  'Johar Town, Lahore',   'Clear Skin Clinic',            '042-2223334444'),
    ('Dr. Rabia Tahir',       'Dermatologist', 15, 'Bahria Town, Lahore',  'Bahria Skin Centre',           '042-2223334445'),
    ('Dr. Faisal Chaudhry',   'Dermatologist', 4,  'Garden Town, Lahore',  'Garden Derm Clinic',           '042-2223334446'),
    ('Dr. Mahwish Akhtar',    'Dermatologist', 20, 'Defence, Lahore',      'Elite Skin Hospital',          '042-2223334447'),

    # ── GENERAL PHYSICIANS ─────────────────────────────────────────
    ('Dr. Usman Ali',         'General Physician', 6,  'Johar Town, Lahore',   'Health Plus Clinic',       '042-3334445550'),
    ('Dr. Nasir Khan',        'General Physician', 9,  'Bahria Town, Lahore',  'Medical Care Center',      '042-3334445551'),
    ('Dr. Asif Mahmood',      'General Physician', 12, 'Gulberg, Lahore',      'Gulberg General Clinic',   '042-3334445552'),
    ('Dr. Rukhsana Begum',    'General Physician', 17, 'Model Town, Lahore',   'Model Town Health Hub',    '042-3334445553'),
    ('Dr. Hamza Iqbal',       'General Physician', 3,  'DHA, Lahore',          'DHA Medical Centre',       '042-3334445554'),
    ('Dr. Saima Bibi',        'General Physician', 8,  'Cantt, Lahore',        'Cantt Family Clinic',      '042-3334445555'),
    ('Dr. Waqas Javed',       'General Physician', 14, 'Iqbal Town, Lahore',   'Iqbal Town Clinic',        '042-3334445556'),
    ('Dr. Amna Shahid',       'General Physician', 5,  'Shadman, Lahore',      'Shadman Health Center',    '042-3334445557'),
    ('Dr. Zahid Hussain',     'General Physician', 21, 'Faisal Town, Lahore',  'Faisal Medical Complex',   '042-3334445558'),
    ('Dr. Kiran Saleem',      'General Physician', 7,  'Township, Lahore',     'Township Clinic',          '042-3334445559'),

    # ── ORTHOPEDIC ─────────────────────────────────────────────────
    ('Dr. Fatima Malik',      'Orthopedic', 15, 'Model Town, Lahore',      'Bone & Joint Hospital',        '042-4445556660'),
    ('Dr. Adnan Cheema',      'Orthopedic', 19, 'DHA, Lahore',             'DHA Ortho Centre',             '042-4445556661'),
    ('Dr. Zafar Iqbal',       'Orthopedic', 25, 'Cantt, Lahore',           'CMH Ortho Department',         '042-4445556662'),
    ('Dr. Mehwish Zahoor',    'Orthopedic', 10, 'Gulberg, Lahore',         'Gulberg Spine Clinic',         '042-4445556663'),
    ('Dr. Pervaiz Ahmad',     'Orthopedic', 13, 'Johar Town, Lahore',      'Johar Bone Clinic',            '042-4445556664'),
    ('Dr. Sundas Bashir',     'Orthopedic', 8,  'Bahria Town, Lahore',     'Bahria Ortho Hospital',        '042-4445556665'),
    ('Dr. Aamir Liaqat',      'Orthopedic', 17, 'Defence, Lahore',         'Defence Joint Care',           '042-4445556666'),
    ('Dr. Lubna Waheed',      'Orthopedic', 6,  'Wapda Town, Lahore',      'Wapda Ortho Clinic',           '042-4445556667'),

    # ── EYE SPECIALISTS ────────────────────────────────────────────
    ('Dr. Bilal Ahmed',       'Eye Specialist', 10, 'Gulberg, Lahore',     'Vision Care Eye Center',       '042-5556667770'),
    ('Dr. Nosheen Arif',      'Eye Specialist', 14, 'DHA, Lahore',         'DHA Eye Hospital',             '042-5556667771'),
    ('Dr. Salman Mirza',      'Eye Specialist', 8,  'Model Town, Lahore',  'Lahore Eye Clinic',            '042-5556667772'),
    ('Dr. Farzana Aziz',      'Eye Specialist', 12, 'Cantt, Lahore',       'Military Eye Centre',          '042-5556667773'),
    ('Dr. Rauf Butt',         'Eye Specialist', 20, 'Bahria Town, Lahore', 'Bahria Eye Hospital',          '042-5556667774'),
    ('Dr. Iram Shafiq',       'Eye Specialist', 6,  'Johar Town, Lahore',  'Johar Eye Clinic',             '042-5556667775'),
    ('Dr. Naveed Qadir',      'Eye Specialist', 16, 'Garden Town, Lahore', 'Garden Eye Centre',            '042-5556667776'),

    # ── NEUROLOGISTS ───────────────────────────────────────────────
    ('Dr. Shoaib Haider',     'Neurologist', 13, 'DHA, Lahore',            'Neuro Care Institute',         '042-6667778880'),
    ('Dr. Uzma Tauqir',       'Neurologist', 17, 'Gulberg, Lahore',        'Brain & Spine Clinic',         '042-6667778881'),
    ('Dr. Danish Rehman',     'Neurologist', 9,  'Model Town, Lahore',     'Model Neuro Centre',           '042-6667778882'),
    ('Dr. Saira Baig',        'Neurologist', 11, 'Cantt, Lahore',          'CMH Neurology Dept',           '042-6667778883'),
    ('Dr. Ahsan Ullah',       'Neurologist', 22, 'Defence, Lahore',        'Defence Neuro Hospital',       '042-6667778884'),
    ('Dr. Mariam Fazal',      'Neurologist', 7,  'Bahria Town, Lahore',    'Bahria Brain Clinic',          '042-6667778885'),
    ('Dr. Rehan Zafar',       'Neurologist', 15, 'Johar Town, Lahore',     'Johar Neurology Clinic',       '042-6667778886'),

    # ── PEDIATRICIANS ──────────────────────────────────────────────
    ('Dr. Asma Yousaf',       'Pediatrician', 12, 'Gulberg, Lahore',       'Kids Health Clinic',           '042-7778889990'),
    ('Dr. Tariq Amin',        'Pediatrician', 8,  'DHA, Lahore',           'DHA Childrens Centre',         '042-7778889991'),
    ('Dr. Sobia Hanif',       'Pediatrician', 16, 'Model Town, Lahore',    'Model Town Kids Clinic',       '042-7778889992'),
    ('Dr. Rizwan Shah',       'Pediatrician', 6,  'Johar Town, Lahore',    'Little Stars Clinic',          '042-7778889993'),
    ('Dr. Nusrat Jabeen',     'Pediatrician', 20, 'Cantt, Lahore',         'CMH Paediatrics Dept',         '042-7778889994'),
    ('Dr. Kamran Latif',      'Pediatrician', 10, 'Bahria Town, Lahore',   'Bahria Kids Hospital',         '042-7778889995'),
    ('Dr. Farah Arshad',      'Pediatrician', 14, 'Defence, Lahore',       'Defence Child Clinic',         '042-7778889996'),
    ('Dr. Zubair Nasir',      'Pediatrician', 5,  'Wapda Town, Lahore',    'Wapda Paeds Clinic',           '042-7778889997'),

    # ── GYNECOLOGISTS ──────────────────────────────────────────────
    ('Dr. Rubina Shaheen',    'Gynecologist', 18, 'Gulberg, Lahore',       'Lady Health Clinic',           '042-8889990000'),
    ('Dr. Naila Tariq',       'Gynecologist', 14, 'DHA, Lahore',           'DHA Women Hospital',           '042-8889990001'),
    ('Dr. Fauzia Malik',      'Gynecologist', 22, 'Model Town, Lahore',    'Mother Care Centre',           '042-8889990002'),
    ('Dr. Shazia Anwar',      'Gynecologist', 9,  'Cantt, Lahore',         'CMH Gynae Dept',               '042-8889990003'),
    ('Dr. Huma Shaukat',      'Gynecologist', 11, 'Bahria Town, Lahore',   'Bahria Women Clinic',          '042-8889990004'),
    ('Dr. Amara Pervez',      'Gynecologist', 7,  'Johar Town, Lahore',    'Johar Lady Clinic',            '042-8889990005'),
    ('Dr. Saadia Omer',       'Gynecologist', 16, 'Defence, Lahore',       'Defence Maternity Hospital',   '042-8889990006'),
    ('Dr. Benish Riaz',       'Gynecologist', 5,  'Garden Town, Lahore',   'Garden Lady Clinic',           '042-8889990007'),

    # ── DENTISTS ───────────────────────────────────────────────────
    ('Dr. Ali Hassan',        'Dentist', 8,  'Gulberg, Lahore',            'Smile Dental Studio',          '042-9990001110'),
    ('Dr. Madiha Rauf',       'Dentist', 12, 'DHA, Lahore',               'DHA Dental Care',              '042-9990001111'),
    ('Dr. Bilal Zafar',       'Dentist', 6,  'Model Town, Lahore',         'Model Dental Clinic',          '042-9990001112'),
    ('Dr. Rafia Ikram',       'Dentist', 15, 'Cantt, Lahore',              'CMH Dental Centre',            '042-9990001113'),
    ('Dr. Adeel Sajid',       'Dentist', 10, 'Bahria Town, Lahore',        'Bahria Smiles Clinic',         '042-9990001114'),
    ('Dr. Sadia Hussain',     'Dentist', 4,  'Johar Town, Lahore',         'Johar Dental Studio',          '042-9990001115'),
    ('Dr. Hamid Nawaz',       'Dentist', 18, 'Defence, Lahore',            'Defence Dental Hospital',      '042-9990001116'),
    ('Dr. Iqra Manzoor',      'Dentist', 7,  'Iqbal Town, Lahore',         'Iqbal Town Dental Clinic',     '042-9990001117'),

    # ── ENT SPECIALISTS ────────────────────────────────────────────
    ('Dr. Mubashir Rana',     'ENT Specialist', 13, 'DHA, Lahore',         'DHA ENT Clinic',               '042-0001112220'),
    ('Dr. Shirin Azam',       'ENT Specialist', 9,  'Gulberg, Lahore',     'Gulberg ENT Centre',           '042-0001112221'),
    ('Dr. Tahir Mehmood',     'ENT Specialist', 17, 'Model Town, Lahore',  'ENT Hospital Lahore',          '042-0001112222'),
    ('Dr. Aisha Nawab',       'ENT Specialist', 6,  'Cantt, Lahore',       'CMH ENT Department',           '042-0001112223'),
    ('Dr. Zeeshan Haider',    'ENT Specialist', 11, 'Bahria Town, Lahore', 'Bahria ENT Clinic',            '042-0001112224'),
    ('Dr. Parveen Akhtar',    'ENT Specialist', 20, 'Johar Town, Lahore',  'Johar ENT Centre',             '042-0001112225'),

    # ── PSYCHIATRISTS ──────────────────────────────────────────────
    ('Dr. Farhan Qadri',      'Psychiatrist', 14, 'DHA, Lahore',           'Mind Care Clinic',             '042-1112223340'),
    ('Dr. Nida Aslam',        'Psychiatrist', 10, 'Gulberg, Lahore',       'Lahore Mental Health Centre',  '042-1112223341'),
    ('Dr. Waseem Akram',      'Psychiatrist', 8,  'Model Town, Lahore',    'Model Psych Clinic',           '042-1112223342'),
    ('Dr. Tasneem Bibi',      'Psychiatrist', 18, 'Cantt, Lahore',         'CMH Psychiatry Dept',          '042-1112223343'),
    ('Dr. Mohsin Raza',       'Psychiatrist', 6,  'Bahria Town, Lahore',   'Bahria Mind Clinic',           '042-1112223344'),
    ('Dr. Samina Ijaz',       'Psychiatrist', 12, 'Defence, Lahore',       'Defence Psych Centre',         '042-1112223345'),

    # ── UROLOGISTS ─────────────────────────────────────────────────
    ('Dr. Naeem Akhtar',      'Urologist', 16, 'DHA, Lahore',              'DHA Urology Clinic',           '042-2223334460'),
    ('Dr. Farrukh Bashir',    'Urologist', 12, 'Gulberg, Lahore',          'Gulberg Kidney Centre',        '042-2223334461'),
    ('Dr. Haseeb Ul Haq',     'Urologist', 20, 'Cantt, Lahore',            'CMH Urology Dept',             '042-2223334462'),
    ('Dr. Zara Salman',       'Urologist', 8,  'Model Town, Lahore',       'Model Urology Clinic',         '042-2223334463'),
    ('Dr. Kashif Mehmood',    'Urologist', 14, 'Bahria Town, Lahore',      'Bahria Urology Centre',        '042-2223334464'),

    # ── GASTROENTEROLOGISTS ────────────────────────────────────────
    ('Dr. Sajid Mahmood',     'Gastroenterologist', 15, 'DHA, Lahore',     'DHA Gastro Clinic',            '042-3334445570'),
    ('Dr. Urooj Fatima',      'Gastroenterologist', 11, 'Gulberg, Lahore', 'Gulberg Gastro Centre',        '042-3334445571'),
    ('Dr. Shahzad Anwar',     'Gastroenterologist', 19, 'Cantt, Lahore',   'CMH Gastro Dept',              '042-3334445572'),
    ('Dr. Mehreen Asghar',    'Gastroenterologist', 7,  'Johar Town, Lahore','Johar Gastro Clinic',        '042-3334445573'),
    ('Dr. Saqib Rasool',      'Gastroenterologist', 13, 'Bahria Town, Lahore','Bahria Gastro Hospital',    '042-3334445574'),

    # ── PULMONOLOGISTS ─────────────────────────────────────────────
    ('Dr. Riaz Ahmad',        'Pulmonologist', 17, 'DHA, Lahore',          'Lahore Lung Centre',           '042-4445556680'),
    ('Dr. Ambreen Khalid',    'Pulmonologist', 10, 'Gulberg, Lahore',      'Gulberg Chest Clinic',         '042-4445556681'),
    ('Dr. Farooq Azam',       'Pulmonologist', 23, 'Cantt, Lahore',        'CMH Chest Dept',               '042-4445556682'),
    ('Dr. Sahar Naqvi',       'Pulmonologist', 8,  'Model Town, Lahore',   'Model Lung Clinic',            '042-4445556683'),
    ('Dr. Shahbaz Gill',      'Pulmonologist', 14, 'Bahria Town, Lahore',  'Bahria Pulmo Centre',          '042-4445556684'),

    # ── ENDOCRINOLOGISTS ───────────────────────────────────────────
    ('Dr. Faisal Nawaz',      'Endocrinologist', 13, 'DHA, Lahore',        'DHA Diabetes Centre',          '042-5556667790'),
    ('Dr. Qurat Ul Ain',      'Endocrinologist', 9,  'Gulberg, Lahore',    'Thyroid Care Clinic',          '042-5556667791'),
    ('Dr. Mansoor Ahmed',     'Endocrinologist', 18, 'Cantt, Lahore',      'CMH Endocrine Dept',           '042-5556667792'),
    ('Dr. Bushra Imtiaz',     'Endocrinologist', 7,  'Model Town, Lahore', 'Model Endo Clinic',            '042-5556667793'),
    ('Dr. Talha Munir',       'Endocrinologist', 15, 'Bahria Town, Lahore','Bahria Diabetes Hospital',     '042-5556667794'),
]

avail_cycle = AVAIL * 10

for i, (name, spec, exp, loc, clinic, phone) in enumerate(doctors):
    em, bg, cl = CARD[spec]
    Doctor.objects.create(
        name=name,
        specialization=spec,
        experience_years=exp,
        location=loc,
        clinic_name=clinic,
        phone=phone,
        availability=avail_cycle[i % len(AVAIL)],
        emoji=em,
        bg_color=bg,
        text_color=cl,
        keywords=KW[spec],
    )

print(f"✅  {Doctor.objects.count()} doctors added successfully!")